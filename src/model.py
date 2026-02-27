from __future__ import annotations
import numpy as np
import pandas as pd
def fit_linear_model(df: pd.DataFrame) -> dict:
    """
    Ajusta un modelo lineal:
    y = a*x + b
    """
    x = df["x"].to_numpy()
    y = df["y"].to_numpy()
    a, b = np.polyfit(x, y, deg=1)
    return {
        "slope": float(a),
        "intercept": float(b)
    }
