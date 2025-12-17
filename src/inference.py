# from joblib import load
# from src.preprocessing import preprocess
# from src.features import create_features

# model = load("models/completion_model.pkl")

# def predict(df):
#     df = preprocess(df)
#     X = create_features(df)
    
#     preds = model.predict(X)
#     probs = model.predict_proba(X)[:, 1]

#     df["completion_prediction"] = preds
#     df["risk_flag"] = probs.apply(
#         lambda x: "HIGH" if x < 0.4 else "MEDIUM" if x < 0.7 else "LOW"
#     )

#     return df
from joblib import load
import pandas as pd
from src.preprocessing import preprocess
from src.features import create_features

model = load("models/completion_model.pkl")

def predict(df):
    df = preprocess(df)
    X = create_features(df)

    preds = model.predict(X)
    probs = model.predict_proba(X)[:, 1]

    df["completion_prediction"] = preds

    # convert numpy array → pandas Series
    probs_series = pd.Series(probs, index=df.index)

    df["risk_flag"] = probs_series.apply(
        lambda x: "HIGH" if x < 0.4 else "MEDIUM" if x < 0.7 else "LOW"
    )

    return df
