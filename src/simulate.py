from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import numpy as np
import pandas as pd

@dataclass
class SimConfig:
    n: int = 3000
    seed: int = 6969
def simulate_data(cfg: SimConfig) -> pd.DataFrame:
    """Genera datos sintéticos"""
    rng = np.random.default_rng(cfg.seed)
    x = rng.normal(loc=0.0, scale=1.0, size=cfg.n)
    noise = rng.normal(loc=0.0, scale=0.6, size=cfg.n)
    y = 2.0 * x + noise
    group = rng.choice(["A", "B"], size=cfg.n, replace=True)
    df = pd.DataFrame({"x": x, "y": y, "group": group})
    return df
def save_raw(df: pd.DataFrame, out_path: str | Path) -> Path:
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)
    return out_path
