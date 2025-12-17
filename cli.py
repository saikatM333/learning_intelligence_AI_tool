import pandas as pd
import argparse
from src.inference import predict
from src.insights import generate_insights

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True)
args = parser.parse_args()

df = pd.read_csv(args.input)
result = predict(df)
insights = generate_insights(result)

print("\nPredictions:")
print(result[["student_id", "completion_prediction", "risk_flag"]])

print("\nInsights:")
for k, v in insights.items():
    print(f"{k}: {v}")
