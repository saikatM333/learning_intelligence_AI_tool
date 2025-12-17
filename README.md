🧠 Learning Intelligence AI Tool

AI-Powered Learning Analytics System for Internship / Training Platforms

📌 Overview

The Learning Intelligence AI Tool is a production-style AI system designed to analyze learner behavior and generate actionable insights for mentors and administrators.

Unlike notebook-based experiments, this project delivers a fully executable AI tool that:

Predicts course completion

Detects early dropout risk

Identifies difficult course chapters

Generates human-readable insights

The system is built with real-world deployment principles, including model persistence, testing, and containerization.

🎯 Key Features
✅ Course Completion Prediction

Binary classification model

Predicts whether a learner will complete a course

⚠️ Early Risk Detection

Probability-based dropout risk flags:

HIGH

MEDIUM

LOW

📚 Chapter Difficulty Detection

Identifies difficult chapters using:

Dropout rate

Average assessment score

Average time spent

📊 Insight Generation

High-risk student list

Key factors affecting completion

Chapters requiring improvement

🧱 System Architecture
Data Input (CSV)
     ↓
Preprocessing
(Median Imputation + Outlier Clipping)
     ↓
Feature Engineering
     ↓
ML Model Inference
     ↓
Insights & Reporting
     ↓
CLI / REST API Output

📂 Project Structure
learning-intelligence-ai/
│
├── app.py                  # FastAPI application
├── cli.py                  # Command Line Interface
├── train_model.py          # Model training & selection
├── generate_data.py        # Synthetic data generator
├── requirements.txt
├── Dockerfile
├── entrypoint.sh
│
├── data/
│   └── sample_students.csv
│
├── models/
│   └── completion_model.pkl
│
├── src/
│   ├── preprocessing.py
│   ├── features.py
│   ├── inference.py
│   ├── insights.py
│   └── __init__.py
│
└── tests/
    └── test_inference.py

📥 Input Format

The system accepts learner data in CSV format with the following fields:

Column Name	Description
student_id	Unique learner ID
course_id	Course identifier
chapter_order	Chapter sequence number
time_spent	Time spent on chapter (minutes)
score	Assessment score
completion_status	1 = completed, 0 = not completed
📤 Output

The AI tool generates:

Course completion predictions

Dropout risk flags

Chapter difficulty scores

Summary insights

Outputs are available via:

REST API (JSON)

CLI (console output)

🤖 Machine Learning Details
Models Evaluated

Logistic Regression

Random Forest

Gradient Boosting

Support Vector Machine (SVM)

Model Selection

Hyperparameter tuning via GridSearchCV

Best model selected based on test accuracy

Class imbalance handled using SMOTE

Preprocessing

Median imputation for missing values

Quantile-based clipping for outlier mitigation

Reproducibility

Trained model is serialized (.pkl)

Loaded during inference

🚀 How to Run (One Command)
Prerequisites

Docker installed

Build the Docker Image
docker build -t learning-ai .

Run the AI Tool
docker run -p 8001:8000 learning-ai

Access API

Open in browser:

http://localhost:8001/docs


Upload sample_students.csv to test predictions.

🧪 Testing

Unit tests written using pytest

Tests are executed automatically when the Docker container starts

API launches only if all tests pass

Run tests manually:

pytest

🛠 CLI Usage (Optional)
python cli.py --input data/sample_students.csv


Outputs predictions and insights to the console.

🔍 Sample Insights

High-risk learners identified early

Low scores and low engagement correlate strongly with dropouts

Certain chapters show consistently higher difficulty

🔐 Ethical AI & Transparency

Synthetic data used for demonstration purposes

No personal or sensitive data included

Model decisions are explainable through insights

🤝 AI Assistance Disclosure

AI tools (including ChatGPT) were used for:

High-level guidance on system architecture

Best practices in ML pipelines and deployment

All core logic, model training, preprocessing, inference, testing, and integration were implemented, verified, and customized independently.

📌 Conclusion

This project demonstrates the ability to:

Build a real AI system (not an experiment)

Integrate ML into a production-style application

Deliver reproducible, testable, and deployable AI solutions

📬 Contact

For any questions or clarifications regarding this project, feel free to reach out.

✅ Ready for Submission

This project fully satisfies the internship assessment requirements for:
AI Engineering · Machine Learning · Real-World Deployment

If you want, I can:

Shorten it (if they prefer concise)

Add screenshots section

Tailor it to a specific company tone

Just tell me 👍