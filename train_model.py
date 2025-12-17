import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from joblib import dump


from src.preprocessing import preprocess
from src.features import create_features

# Load and preprocess data
df = pd.read_csv("data/sample_students.csv")
df = preprocess(df)

X = create_features(df)
y = df["completion_status"]

# Stratified train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Apply SMOTE ONLY on training data


# Models and hyperparameters
models = {
    "logistic": (
        LogisticRegression(max_iter=1000),
        {"C": [0.1, 1, 10]}
    ),
    "random_forest": (
        RandomForestClassifier(random_state=42),
        {"n_estimators": [100, 200], "max_depth": [None, 10]}
    ),
    "gradient_boosting": (
        GradientBoostingClassifier(),
        {"n_estimators": [100, 200], "learning_rate": [0.05, 0.1]}
    ),
    "svm": (
        SVC(probability=True),
        {"C": [0.5, 1, 5], "kernel": ["rbf"]}
    )
}

best_model = None
best_score = 0
best_name = ""

# Grid search for each model
for name, (model, params) in models.items():
    grid = GridSearchCV(
        model,
        params,
        cv=5,
        scoring="accuracy",
        n_jobs=-1
    )
    grid.fit(X_train, y_train)

    preds = grid.best_estimator_.predict(X_test)
    score = accuracy_score(y_test, preds)

    print(f"{name} accuracy: {score:.4f}")

    if score > best_score:
        best_score = score
        best_model = grid.best_estimator_
        best_name = name

# Save the best model
dump(best_model, "models/completion_model.pkl")

print("\nBest Model Selected:", best_name)
print("Best Accuracy:", round(best_score, 4))
print("Best model saved successfully.")
