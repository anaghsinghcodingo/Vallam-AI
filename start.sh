#!/bin/bash

# VallamAI Deployment Script
echo "🚀 Starting VallamAI Deployment..."

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

# Start the application
echo "🏁 Starting VallamAI application..."
python app.py
