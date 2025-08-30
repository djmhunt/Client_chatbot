# Client chat

A web application designed for psychology students to practice Cognitive Behavioral Therapy (CBT) skills with realistic AI-simulated clients. Each client presents mental health conditions and communication patterns to provide valuable training experience.

## Features

- 🎓 **Educational Focus**: Designed for CBT training and psychology education
- 👥 **Multiple Clients**: 5 different simulated clients with various mental health conditions
- 🧠 **Realistic Presentations**: Authentic symptom presentations and communication styles
- 🎨 **Modern Interface**: Clean, professional chat interface optimized for therapeutic practice
- 📋 **Client Profiles**: Detailed background information for each simulated client
- 🔐 **Secure API Handling**: Server-side Claude API integration with no client-side exposure
- 📄 **Session Documentation**: PDF export functionality for training records and supervision
- 📱 **Mobile-Friendly**: Responsive design works on all devices
- ⚡ **Fast Performance**: Flask backend optimized for educational use

## Available Clients

The application includes multiple simulated clients, each presenting different mental health conditions and communication styles. Each client has been carefully designed to provide authentic training experiences for specific CBT techniques and therapeutic approaches.

**Current clients include:**
- Anxiety disorders (generalized anxiety, social anxiety, panic disorder)
- Mood disorders (major depression)
- Obsessive-compulsive disorder
- Various age groups and backgrounds

For detailed information about each client, including their background, age, condition, and personality characteristics, see the individual JSON files in the `personalities/` directory. Each file contains comprehensive information about the client's presentation, symptoms, and communication style.

**To explore available clients:**
1. Browse the `personalities/` folder in this repository
2. Open any `.json` file to see detailed client information
3. Or launch the application and use the "Select Client" interface

## Quick Setup

### 1. Get Your Claude API Key

1. Visit [console.anthropic.com](https://console.anthropic.com/)
2. Sign up or log in to your account
3. Navigate to "API Keys" in your dashboard
4. Create a new API key
5. Copy the API key (starts with `sk-ant-`)

### 2. Local Development

```bash
# Clone the repository
git clone https://github.com/djmhunt/Client_chatbot.git
cd Client_chatbot

# Set up Python environment (recommended)
conda create -n cbt-simulator python=3.11
conda activate cbt-simulator

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Open your browser and go to `http://localhost:8000`

### 3. Using the Application

1. **Enter your Claude API key** when prompted
2. **Select a client** from the dropdown menu
3. **Begin your practice session** - each client will start with a realistic opening
4. **Practice CBT techniques** through natural conversation
5. **Export sessions as PDF** for supervision and review
6. **Start new sessions** to practice consistency across multiple interactions

### 4. Azure Deployment

#### Option A: Deploy to Azure App Service

1. **Fork/Clone this repository**

2. **Create Azure App Service:**
   - Go to [Azure Portal](https://portal.azure.com/)
   - Create a new "App Service"
   - Choose Python 3.11 runtime
   - Select your subscription and resource group

3. **Deploy from GitHub:**
   - In App Service → Deployment Center
   - Connect to your GitHub repository
   - Azure will automatically deploy using the included configuration

4. **Access your app:**
   - Your app will be available at: `https://yourappname.azurewebsites.net`

## Customizing Content

### Adding New Clients

1. **Create a new JSON file** in the `personalities/` directory:
```json
{
  "name": "ClientName",
  "condition": "Mental Health Condition",
  "age": 25,
  "background": "Brief background description",
  "personality": "Detailed personality prompt for AI..."
}
```

2. **Restart the application** - new clients will automatically appear in the selector

### Customizing Initial Messages

1. **Edit `start_messages.txt`** - add one message per line
2. **Messages are randomly selected** when clients begin sessions
3. **No code changes needed** - updates take effect immediately

### Modifying Client Presentations

1. **Edit JSON files** in the `personalities/` directory
2. **Update the `personality` field** to modify AI behavior
3. **Adjust `background` and `condition`** for different scenarios

#### Option B: Azure Container Instances (Advanced)

1. **Build Docker image** (Dockerfile included)
2. **Push to Azure Container Registry**
3. **Deploy to Container Instances**

## File Structure

```
Client_chatbot/
├── app.py                          # Main Flask application
├── main.py                         # Azure entry point
├── requirements.txt                # Python dependencies
├── runtime.txt                     # Python version for Azure
├── Procfile                        # Process configuration
├── index.html                      # CBT training interface
├── script.js                       # Frontend JavaScript
├── styles.css                      # Professional styling
├── start_messages.txt              # Random client opening messages
├── personalities/                  # Client personality definitions
├── .gitignore                      # Git ignore rules
└── README.md                       # This file
```

## API Endpoints

- `GET /` - Serves the main application
- `GET /api/personalities` - Lists available clients
- `GET /api/personality/<id>` - Gets specific client details
- `GET /api/start-message` - Returns random opening message
- `POST /api/claude` - Proxies requests to Claude API
- `GET /health` - Health check for monitoring

## Technical Details

### Backend (Flask)
- **Client Management**: Loads personality profiles from JSON files
- **Message Randomization**: Server-side selection of opening messages
- **API Proxy**: Secure Claude API integration without CORS issues
- **Health Monitoring**: Built-in health check endpoint
- **Educational Focus**: Optimized for training scenarios

### Frontend (Vanilla JavaScript)
- **Client Selection**: Professional interface for choosing practice clients
- **Session Management**: Clean session boundaries between different clients
- **PDF Generation**: Professional documentation for training records
- **Responsive Design**: Works on laptops, tablets, and phones
- **Accessibility**: Keyboard navigation and screen reader friendly

### Educational Design
- **Realistic Presentations**: Authentic mental health symptom portrayals
- **Varied Conditions**: Multiple diagnosis categories for comprehensive training
- **Professional Context**: Designed specifically for CBT education
- **Supervision Support**: PDF exports for instructor review

## Troubleshooting

### Common Issues

1. **Python dependencies not found:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Port already in use:**
   - Flask automatically finds an available port
   - Check for other running applications on port 8000

3. **API key errors:**
   - Verify your Claude API key format (starts with `sk-ant-`)
   - Check API key permissions in [Anthropic console](https://console.anthropic.com/)
   - Ensure you have sufficient API credits

4. **Client personalities not loading:**
   - Check that all JSON files in `personalities/` directory are valid
   - Verify file permissions for the personalities directory

5. **Start messages not working:**
   - Ensure `start_messages.txt` exists and has content
   - Check that file contains one message per line

### Development Issues

1. **Flask import errors:**
   ```bash
   conda activate your-environment
   pip install flask anthropic
   ```

2. **JSON parsing errors:**
   - Validate JSON files using an online JSON validator
   - Check for trailing commas or syntax errors

3. **File not found errors:**
   - Ensure all files are in the correct directory structure
   - Check file paths are relative to the app.py location

### Azure Deployment Issues

- **Logs:** Check in Azure Portal → App Service → Log stream
- **Configuration:** All config is in the application files
- **Dependencies:** Ensure `requirements.txt` is up to date
- **Python Version:** Verify `runtime.txt` specifies Python 3.11

### Educational Use Tips

1. **For Instructors:**
   - Review exported PDF sessions for student assessment
   - Customize personality files for specific learning objectives
   - Monitor student API usage through Claude console

2. **For Students:**
   - Practice with different clients to understand varied presentations
   - Export sessions for self-reflection and improvement
   - Use clear session boundaries between different practice scenarios

3. **Technical Support:**
   - Check browser console for JavaScript errors
   - Verify network connectivity for API calls
   - Test with different browsers if issues persist

## Educational Context

This application is specifically designed for **undergraduate psychology education** and **CBT training programs**. It provides:

- **Safe Practice Environment**: Students can make mistakes without real-world consequences
- **Consistent Training**: Each client maintains character consistency across sessions
- **Diverse Experience**: Multiple conditions provide comprehensive training
- **Documentation**: PDF exports support supervision and assessment
- **Accessibility**: Available 24/7 for flexible learning schedules

## Rate Limits & Costs

- Claude API has usage-based pricing - check [Anthropic pricing](https://www.anthropic.com/pricing)
- Typical training session costs are minimal (usually under $0.10 per session)
- Rate limits depend on your Anthropic subscription tier
- The application includes timeout handling for robust operation

## Security & Privacy

- **API Keys**: Processed server-side only, never exposed to client
- **Session Data**: Not stored permanently, exists only during active sessions
- **Educational Compliance**: Designed for educational use, not real therapy
- **No Personal Data**: Simulated clients only, no real patient information

## License

This project is open source and available under the MIT License.

## Contributing

Educational improvements and additional client personalities are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Test thoroughly with educational scenarios
4. Submit a pull request with clear documentation

## Support

For educational institutions interested in customizing this platform or integrating it into their curriculum, please reach out through the GitHub repository.
