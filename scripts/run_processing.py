from pathlib import Path
import pandas as pd
from src.process import process_data, save_processed, summarize
def main() -> None:
    raw_path = Path("data/raw/simulated_data.csv")
    processed_path = Path("data/processed/processed_data.csv")
    summary_path = Path("results/tables/summary_by_group.csv")
    df_raw = pd.read_csv(raw_path)
    df_proc = process_data(df_raw)
    save_processed(df_proc, processed_path)
    summary = summarize(df_proc)
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(summary_path, index=False)
    print(f"[OK] Datos procesados: {processed_path}")
    print(f"[OK] Tabla resumen: {summary_path}")
if __name__ == "__main__":
    main()
