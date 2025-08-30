# Chat with Sarah - Claude API Chatbot

A beautiful, responsive web application that creates a chat interface with an AI personality powered by Claude API. Built with Flask for reliable deployment on Azure.

## Features

- 🎨 Modern, responsive chat interface
- 🤖 Pre-defined AI personality (Sarah - friendly virtual assistant)
- 🔐 Secure API key handling through backend proxy
- 💬 Real-time typing indicators
- 📱 Mobile-friendly design
- 🧹 Clear chat functionality
- ⚡ Fast and reliable Flask backend
- ☁️ Azure-ready deployment

## Quick Setup

### 1. Get Your Claude API Key

1. Visit [console.anthropic.com](https://console.anthropic.com/)
2. Sign up or log in to your account
3. Navigate to "API Keys" in your dashboard
4. Create a new API key
5. Copy the API key (starts with `sk-ant-`)

### 2. Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Open your browser and go to `http://localhost:8000`

### 3. Azure Deployment

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

#### Option B: Azure Container Instances (Advanced)

1. **Build Docker image** (Dockerfile included)
2. **Push to Azure Container Registry**
3. **Deploy to Container Instances**

## Configuration Files

### For Azure App Service:
- `requirements.txt` - Python dependencies
- `main.py` - Azure entry point
- `app.py` - Flask application
- `runtime.txt` - Python version specification

### For Security:
- API keys are handled server-side only
- No CORS issues - proper backend proxy
- No client-side API key exposure

## File Structure

```
Client_chatbot/
├── app.py              # Main Flask application
├── main.py             # Azure entry point
├── requirements.txt    # Python dependencies
├── runtime.txt         # Python version for Azure
├── Procfile           # Process configuration
├── index.html         # Chat interface
├── script.js          # Frontend JavaScript
├── styles.css         # Styling
├── personality.txt    # AI personality definition
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## Technical Details

### Backend (Flask)
- Serves static files (HTML, CSS, JS)
- Proxies requests to Claude API (eliminates CORS issues)
- Handles API key securely on server-side
- Includes health check endpoint for monitoring

### Frontend (Vanilla JavaScript)
- Clean, modern chat interface
- Real-time typing indicators
- Responsive design for all devices
- Local storage for API key (sent to backend only)

### Security
- API keys processed server-side only
- CORS properly handled by Flask-CORS
- No direct client-to-API communication
- Secure request forwarding

## Troubleshooting

### Common Issues

1. **Flask import errors during local development:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Port already in use:**
   - Flask automatically finds an available port
   - Check for other running applications

3. **API key errors:**
   - Verify your Claude API key format
   - Check API key permissions in Anthropic console

4. **Azure deployment issues:**
   - Check Azure logs in the portal
   - Verify all required files are committed to Git
   - Ensure Python version matches runtime.txt

### Azure-Specific

- **Logs:** Check in Azure Portal → App Service → Log stream
- **Configuration:** All config is in the application files
- **Scaling:** Azure handles this automatically
- **Custom Domain:** Configure in Azure Portal if needed

### Rate Limits

- Claude API has rate limits based on your subscription
- The Flask backend includes proper timeout handling
- Azure provides automatic scaling for high traffic

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to fork this project and submit pull requests for improvements!
