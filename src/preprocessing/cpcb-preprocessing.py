from pathlib import Path
import pandas as pd

raw_dir = Path("datasets/cpcb/PM2.5")
all_dfs = []

for city_folder in raw_dir.iterdir():
    if city_folder.is_dir():
        for file in city_folder.glob("*.csv"):
            try:
                df = pd.read_csv(file)
                df["City"] = city_folder.name
                df["Year"] = file.stem
                all_dfs.append(df)
            except Exception as e:
                print(f"Error reading {file}: {e}")

# Combine all into one big DataFrame
df_all = pd.concat(all_dfs, ignore_index=True)

# Save for further cleaning
df_all.to_csv("datasets/cpcb/processed/all_pm25_combined.csv", index=False)
