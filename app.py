from fastapi import FastAPI, UploadFile
import pandas as pd
from src.inference import predict
from src.insights import generate_insights

app = FastAPI(title="Learning Intelligence AI Tool")

@app.post("/analyze")
async def analyze(file: UploadFile):
    df = pd.read_csv(file.file)
    result = predict(df)
    insights = generate_insights(result)

    return {
        "predictions": result.to_dict(orient="records"),
        "insights": insights
    }
