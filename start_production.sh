#!/bin/bash

# VallamAI Production Deployment Script
echo "🚀 Starting VallamAI Production Deployment..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found. Please copy .env.example to .env and configure your API key."
    echo "   cp .env.example .env"
    exit 1
fi

# Set production environment
export FLASK_ENV=production
export FLASK_DEBUG=False

# Start with Gunicorn
echo "🏁 Starting VallamAI with Gunicorn..."
gunicorn -c gunicorn_config.py app:app
