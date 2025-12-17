#!/bin/bash
set -e

echo "=============================="
echo "🚀 Starting AI Tool Pipeline"
echo "=============================="

echo "📊 Generating synthetic data..."
python generate_data.py

echo "🤖 Training ML model..."
python train_model.py

echo "🧪 Running unit tests..."
pytest

echo "✅ Tests passed successfully"

echo "🌐 Starting FastAPI server..."
python -m uvicorn app:app --host 0.0.0.0 --port $PORT
