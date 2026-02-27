from __future__ import annotations
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
def plot_scatter(df: pd.DataFrame, out_path: str | Path, title: str = "Relación X vs Y") -> Path:
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.figure()
    plt.scatter(df["x"], df["y"], s=14, alpha=0.7)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(out_path, dpi=160)
    plt.close()
    return out_path
