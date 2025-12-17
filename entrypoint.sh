#!/bin/bash
set -e

if [ ! -f models/completion_model.pkl ]; then
    echo "📊 Model not found. Generating data..."
    python generate_data.py

    echo "🤖 Training ML model..."
    python train_model.py

    echo "🧪 Running tests..."
    pytest
else
    echo "✅ Model already exists. Skipping training."
fi

echo "🚀 Starting FastAPI..."
python -m uvicorn app:app --host 0.0.0.0 --port ${PORT}
