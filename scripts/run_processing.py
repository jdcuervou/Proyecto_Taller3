from pathlib import Path
import pandas as pd
from src.process import process_data, save_processed, summarize
from src.model import fit_linear_model

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

    # Modelo
    params = fit_linear_model(df_proc)
    coeffs_path = Path("results/tables/model_coeffs.csv")
    coeffs_path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([params]).to_csv(coeffs_path, index=False)

    print(f"Datos procesados: {processed_path}")
    print(f"Tabla resumen: {summary_path}")
    print(f"Coeficientes del modelo: {coeffs_path}")

if __name__ == "__main__":
    main()
