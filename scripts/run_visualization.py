from pathlib import Path
import pandas as pd
from src.visualize import plot_scatter
def main() -> None:
    processed_path = Path("data/processed/processed_data.csv")
    fig_path = Path("results/figures/scatter_xy.png")
    df_proc = pd.read_csv(processed_path)
    out = plot_scatter(
    df_proc,
    fig_path,
    title="Relación X vs Y - visualización paleativa")
    print(f"Figura guardada: {out}")
if __name__ == "__main__":
    main()
