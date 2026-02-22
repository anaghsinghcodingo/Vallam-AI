# VallamAI - Kerala Snake Boat Intelligence Platform

🏆 **AI-Powered Snake Boat Race Analytics for Kerala's Chundan Vallam Tradition**

VallamAI is an advanced analytics platform that combines physics-based simulation with AI analysis to provide strategic insights for Kerala's legendary snake boat races.

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Google Generative AI API Key

### Installation & Setup

1. **Clone or Download** the project files
2. **Set up environment:**
   ```bash
   # Copy environment template
   cp .env.example .env
   
   # Edit .env and add your Google API key
   # Get your key from: https://makersuite.google.com/app/apikey
   ```

3. **Run the deployment script:**
   
   **For Windows:**
   ```cmd
   start.bat
   ```
   
   **For Linux/Mac:**
   ```bash
   chmod +x start.sh
   ./start.sh
   ```

4. **Open your browser** and navigate to `http://localhost:5000`

## 📁 Project Structure

```
Vallam AI/
├── app.py                 # Flask backend server
├── VallamAI.html          # Frontend application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── start.bat             # Windows startup script
├── start.sh              # Linux/Mac startup script
├── start_production.sh   # Production deployment script
├── gunicorn_config.py   # Gunicorn configuration
└── README.md             # This file
```

## ⚙️ Configuration

### Environment Variables (.env)

```env
# Required: Google Generative AI API Key
GOOGLE_API_KEY=your_google_api_key_here

# Flask Configuration
FLASK_ENV=production
FLASK_DEBUG=False

# Server Configuration
HOST=0.0.0.0
PORT=5000

# CORS Configuration (for production, specify your domain)
CORS_ORIGINS=*
```

## 🌐 Deployment Options

### Development Mode
Use the basic startup scripts for development:
- Windows: `start.bat`
- Linux/Mac: `start.sh`

### Production Mode
For production deployment:
```bash
chmod +x start_production.sh
./start_production.sh
```

This uses Gunicorn WSGI server with optimized settings for production.

### Docker Deployment (Optional)
Create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["gunicorn", "-c", "gunicorn_config.py", "app:app"]
```

## 🔧 API Endpoint

### POST /simulate
Runs the boat race simulation and AI analysis.

**Request Body:**
```json
{
  "boat_length": 35,
  "num_rowers": 100,
  "force_per_rower": 180,
  "stroke_rate": 32,
  "wind_speed": 12,
  "wind_direction": 90,
  "water_current": 0.8
}
```

**Response:**
```json
{
  "simulation": {
    "race_time": 245.67,
    "final_velocity": 4.2,
    "average_velocity": 4.07,
    "max_velocity": 4.8,
    "final_fatigue_factor": 0.6134
  },
  "ai_analysis": "AI-generated strategic insights..."
}
```

## 🎯 Features

- **Real-time Simulation**: Physics-based hydrodynamic modeling
- **AI Analysis**: Google Gemini-powered strategic recommendations
- **Interactive UI**: Modern, responsive web interface
- **Dynamic Calculations**: Live parameter adjustments
- **Visual Analytics**: Charts, graphs, and seating layouts

## 🔬 Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **AI Engine**: Google Generative AI (Gemini)
- **Simulation**: NumPy Physics Calculations
- **Deployment**: Gunicorn (Production)

## 🐛 Troubleshooting

### Common Issues

1. **"GOOGLE_API_KEY not found"**
   - Ensure you've created `.env` from `.env.example`
   - Add your valid Google API key to the `.env` file

2. **ModuleNotFoundError**
   - Run `pip install -r requirements.txt` to install dependencies

3. **Port already in use**
   - Change PORT in `.env` file or stop conflicting services

4. **CORS issues in production**
   - Set `CORS_ORIGINS` to your specific domain in `.env`

### Logs and Debugging

- Development mode shows detailed Flask logs
- Production mode uses Gunicorn logging
- Check browser console for frontend issues

## 📈 Performance Notes

- **Development**: Single-threaded Flask server
- **Production**: Multi-worker Gunicorn (4 workers by default)
- **Memory**: ~100MB base usage + AI model loading
- **Response Time**: ~2-5 seconds for AI analysis

## 🔒 Security Considerations

- Keep your Google API key secure (never commit to version control)
- Use HTTPS in production
- Restrict CORS origins in production
- Consider rate limiting for API endpoints

## 📞 Support

For issues and questions:
1. Check this README and troubleshooting section
2. Verify your API key and environment setup
3. Review browser console for frontend errors

## 🏁 License

This project is a hackathon prototype demonstrating AI integration with traditional Kerala boat racing analytics.

---

**Built with ❤️ for Kerala's Snake Boat Racing Tradition**
