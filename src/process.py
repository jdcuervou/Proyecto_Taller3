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
    """Resumen"""
    summary = (
        df.groupby("group", as_index=False)
        .agg(
            n=("x", "size"),
            x_mean=("x", "mean"),
            y_mean=("y", "mean"),
            residual_mean=("residual", "mean"),
      )
    )
    return summary
def save_processed(df: pd.DataFrame, out_path: str | Path) -> Path:
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)
    return out_path
