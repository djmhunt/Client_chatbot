from flask import Flask, request, jsonify, send_from_directory
import os
import json
import anthropic
import random

app = Flask(__name__, static_folder='.', static_url_path='')

# Claude API configuration
CLAUDE_MODEL = "claude-sonnet-4-20250514"
PERSONALITIES_DIR = "personalities"

@app.route('/')
def index():
    """Serve the main HTML file"""
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def static_files(filename):
    """Serve static files (CSS, JS, etc.)"""
    return send_from_directory('.', filename)

@app.route('/api/personalities')
def get_personalities():
    """Get list of available personalities"""
    try:
        personalities = []
        personalities_path = os.path.join(os.path.dirname(__file__), PERSONALITIES_DIR)
        
        if os.path.exists(personalities_path):
            for filename in os.listdir(personalities_path):
                if filename.endswith('.json'):
                    filepath = os.path.join(personalities_path, filename)
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            personality_data = json.load(f)
                            personalities.append({
                                'id': filename[:-5],  # Remove .json extension
                                'name': personality_data.get('name', 'Unknown'),
                                'condition': personality_data.get('condition', 'Unknown'),
                                'age': personality_data.get('age', 'Unknown'),
                                'background': personality_data.get('background', '')
                            })
                    except Exception as e:
                        print(f"Error loading personality file {filename}: {e}")
                        continue
        
        return jsonify({'personalities': personalities})
    except Exception as e:
        return jsonify({'error': {'message': f'Failed to load personalities: {str(e)}'}}), 500

@app.route('/api/personality/<personality_id>')
def get_personality(personality_id):
    """Get a specific personality by ID"""
    try:
        personalities_path = os.path.join(os.path.dirname(__file__), PERSONALITIES_DIR)
        filepath = os.path.join(personalities_path, f"{personality_id}.json")
        
        if not os.path.exists(filepath):
            return jsonify({'error': {'message': 'Personality not found'}}), 404
        
        with open(filepath, 'r', encoding='utf-8') as f:
            personality_data = json.load(f)
        
        return jsonify(personality_data)
    except Exception as e:
        return jsonify({'error': {'message': f'Failed to load personality: {str(e)}'}}), 500

@app.route('/api/config')
def get_config():
    """Get configuration settings including Claude model"""
    return jsonify({'model': CLAUDE_MODEL})

@app.route('/api/start-message')
def get_start_message():
    """Get a randomly selected initial message"""

    fallback_messages = ["Hello... I'm here because someone suggested I should talk to someone. I'm not really sure how this works.",
                         "Hi. I was told this might help, though I'm honestly not sure about any of this.",
                         "Hello. I'm here because I think I need to talk to someone about what I've been going through."
                        ]
    
    try:
        start_messages_path = os.path.join(os.path.dirname(__file__), 'start_messages.txt')
        
        if not os.path.exists(start_messages_path):
            # Fallback messages if file doesn't exist
            selected_message = random.choice(fallback_messages)
            return jsonify({'message': selected_message})
        
        with open(start_messages_path, 'r', encoding='utf-8') as f:
            messages = [line.strip() for line in f.readlines() if line.strip()]
        
        if not messages:
            # Fallback if file is empty
            fallback_message = fallback_messages[0]
            return jsonify({'message': fallback_message})
        
        selected_message = random.choice(messages)
        return jsonify({'message': selected_message})
        
    except Exception as e:
        # Return fallback message on error
        fallback_message = fallback_messages[0]
        return jsonify({'message': fallback_message})

@app.route('/api/claude', methods=['POST'])
def claude_proxy():
    """Proxy requests to Claude API using the anthropic client"""
    try:
        # Get the request data
        data = request.get_json()
        
        if not data:
            return jsonify({'error': {'message': 'No data provided'}}), 400
        
        # Extract API key from request
        api_key = data.get('api_key')
        if not api_key:
            return jsonify({'error': {'message': 'API key is required'}}), 400
        
        # Initialize Anthropic client with the provided API key
        client = anthropic.Anthropic(api_key=api_key)
        
        # Extract message data
        messages = data.get('messages', [])
        system_prompt = data.get('system', '')
        max_tokens = data.get('max_tokens', 1000)
        model = data.get('model', CLAUDE_MODEL)
        
        if not messages:
            return jsonify({'error': {'message': 'Messages are required'}}), 400
        
        # Make request to Claude API using the anthropic client
        response = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            system=system_prompt,
            messages=messages
        )
        
        # Convert response to dict format that matches the expected API response
        content_blocks = []
        for content in response.content:
            if content.type == 'text':
                content_blocks.append({'type': content.type, 'text': content.text})
            elif content.type == 'tool_use':
                content_blocks.append({
                    'type': content.type, 
                    'id': content.id,
                    'name': content.name,
                    'input': content.input
                })
            else:  # Other types, handle gracefully
                content_blocks.append({'type': content.type})
        
        response_data = {
            'id': response.id,
            'type': response.type,
            'role': response.role,
            'content': content_blocks,
            'model': response.model,
            'stop_reason': response.stop_reason,
            'stop_sequence': response.stop_sequence,
            'usage': {
                'input_tokens': response.usage.input_tokens,
                'output_tokens': response.usage.output_tokens
            }
        }
        
        return jsonify(response_data)
            
    except anthropic.AuthenticationError as e:
        return jsonify({'error': {'message': 'Invalid API key', 'type': 'authentication_error'}}), 401
    except anthropic.PermissionDeniedError as e:
        return jsonify({'error': {'message': 'Permission denied', 'type': 'permission_error'}}), 403
    except anthropic.NotFoundError as e:
        return jsonify({'error': {'message': 'Resource not found', 'type': 'not_found_error'}}), 404
    except anthropic.RateLimitError as e:
        return jsonify({'error': {'message': 'Rate limit exceeded', 'type': 'rate_limit_error'}}), 429
    except anthropic.BadRequestError as e:
        return jsonify({'error': {'message': f'Bad request: {str(e)}', 'type': 'invalid_request_error'}}), 400
    except anthropic.APIError as e:
        return jsonify({'error': {'message': f'API error: {str(e)}', 'type': 'api_error'}}), 500
    except Exception as e:
        return jsonify({'error': {'message': f'Server error: {str(e)}', 'type': 'server_error'}}), 500

@app.route('/health')
def health_check():
    """Health check endpoint for Azure"""
    return jsonify({'status': 'healthy', 'service': 'claude-chatbot'})

if __name__ == '__main__':
    # For local development
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=True)
