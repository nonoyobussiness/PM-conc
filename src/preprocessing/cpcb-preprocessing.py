import pandas as pd
from pathlib import Path

# Create output folder
Path("datasets/cpcb/processed").mkdir(parents=True, exist_ok=True)

# Where raw files live
raw_dir = Path("datasets/cpcb/PM2.5")
all_dfs = []

# Step 1: Loop through cities and years
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

# Step 2: Combine all raw data
df = pd.concat(all_dfs, ignore_index=True)

# Step 3: Clean & Extract PM2.5

# Convert Timestamp to datetime
if "Timestamp" in df.columns:
    df["date"] = pd.to_datetime(df["Timestamp"], errors="coerce")
else:
    raise ValueError("❌ 'Timestamp' column not found!")

# Drop missing dates
df = df.dropna(subset=["date"])

# Filter valid PM2.5
pm_col = "PM2.5 (µg/m³)"
if pm_col not in df.columns:
    raise ValueError(f"❌ '{pm_col}' column not found!")

# Drop rows where PM2.5 is missing or invalid
df = df[df[pm_col].between(5, 1000)]

# Step 4: Group by date and city (or station if available)
group_cols = ["date", "City"]
if "Station Name" in df.columns and "Latitude" in df.columns and "Longitude" in df.columns:
    group_cols = ["date", "Station Name", "Latitude", "Longitude"]

df_daily = (
    df.groupby(group_cols)[pm_col]
    .mean()
    .reset_index()
    .rename(columns={pm_col: "PM2.5"})
)

# Step 5: Save
df_daily.to_csv("datasets/cpcb/processed/cpcb_pm25_daily.csv", index=False)

print("✅ Cleaned PM2.5 saved at: datasets/cpcb/processed/cpcb_pm25_daily.csv")
