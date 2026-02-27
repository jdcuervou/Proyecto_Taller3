from pathlib import Path
from src.simulate import SimConfig, save_raw, simulate_data
def main() -> None:
    raw_path = Path("data/raw/simulated_data.csv")
    df = simulate_data(SimConfig(n=300, seed=7))
    out = save_raw(df, raw_path)
    print(f"[OK] Datos guardados: {out}")
if __name__ == "__main__":
    main()
