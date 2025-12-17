import sys
import os

sys.path.append(os.path.abspath("."))

import pandas as pd
from src.inference import predict

def test_prediction():
    df = pd.DataFrame({
        "time_spent": [10],
        "score": [30]
    })

    result = predict(df)
    assert "completion_prediction" in result.columns
