from __future__ import annotations
from pathlib import Path
import pandas as pd
def process_data(df: pd.DataFrame) -> pd.DataFrame:
    """Limpiar y crear variables"""
    out = df.copy()
    out = out.dropna()
    out["y_hat_simple"] = 2.0 * out["x"]  # predicción
    out["residual"] = out["y"] - out["y_hat_simple"]
    return out
def summarize(df: pd.DataFrame) -> pd.DataFrame:
    def corr_xy(g: pd.DataFrame) -> float:
        return float(g["x"].corr(g["y"]))
    summary = (
        df.groupby("group", as_index=False)
        .apply(lambda g: pd.Series({
            "n": g["x"].size,
            "x_mean": g["x"].mean(),
            "y_mean": g["y"].mean(),
            "residual_mean": g["residual"].mean(),
            "corr_xy": corr_xy(g),
        }))
        .reset_index(drop=True)
    )
    return summary
def save_processed(df: pd.DataFrame, out_path: str | Path) -> Path:
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)
    return out_path
