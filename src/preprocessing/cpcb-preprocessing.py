import pandas as pd
from pathlib import Path

# 📁 Create output folder
Path("datasets/cpcb/processed").mkdir(parents=True, exist_ok=True)

# 📁 Where raw city data lives
raw_dir = Path("datasets/cpcb/PM2.5")
all_dfs = []

# 📌 Step 1: Loop through city folders and read each CSV
for city_folder in raw_dir.iterdir():
    if city_folder.is_dir():
        for file in city_folder.glob("*.csv"):
            try:
                df = pd.read_csv(file)
                df["City"] = city_folder.name
                df["Year"] = file.stem
                all_dfs.append(df)
            except Exception as e:
                print(f"❌ Error reading {file}: {e}")

# 🔄 Step 2: Combine all files
df = pd.concat(all_dfs, ignore_index=True)

# 🧹 Step 3: Parse timestamp
if "Timestamp" in df.columns:
    df["date"] = pd.to_datetime(df["Timestamp"], errors="coerce")
else:
    raise ValueError("❌ 'Timestamp' column not found!")

# Drop missing dates
df = df.dropna(subset=["date"])

# 🧪 Step 4: Filter valid PM2.5 readings
pm_col = "PM2.5 (µg/m³)"
if pm_col not in df.columns:
    raise ValueError(f"❌ '{pm_col}' column not found!")

df = df[df[pm_col].between(5, 1000)]  # reasonable range

# 📊 Step 5: Group by date + city or station (if available)
group_cols = ["date", "City"]
if {"Station Name", "Latitude", "Longitude"}.issubset(df.columns):
    group_cols = ["date", "Station Name", "Latitude", "Longitude"]

df_daily = (
    df.groupby(group_cols)[pm_col]
    .mean()
    .reset_index()
    .rename(columns={pm_col: "PM2.5"})
)

# 📍 Step 6: Add coordinates for cities (only if city-based format is used)
if "Latitude" not in df_daily.columns:
    # City to lat/lon lookup
    city_coords = pd.DataFrame({
        "City": [
            "Ahmedabad", "Bengaluru", "Bhubaneswar", "Chennai", "Delhi",
            "Hyderabad", "Imphal", "Jaipur", "Kolkata", "Lucknow",
            "Mumbai", "Shillong", "Vizag"
        ],
        "Lat": [
            23.0225, 12.9716, 20.2961, 13.0827, 28.6139,
            17.3850, 24.8170, 26.9124, 22.5726, 26.8467,
            19.0760, 25.5788, 17.6868
        ],
        "Lon": [
            72.5714, 77.5946, 85.8245, 80.2707, 77.2090,
            78.4867, 93.9368, 75.7873, 88.3639, 80.9462,
            72.8777, 91.8933, 83.2185
        ]
    })

    # Merge coordinates into daily data
    df_daily = df_daily.merge(city_coords, on="City", how="left")
    df_daily = df_daily.rename(columns={"Lat": "Latitude", "Lon": "Longitude"})
    df_daily = df_daily.dropna(subset=["Latitude", "Longitude"])

# 💾 Step 7: Save processed CSV
output_path = "datasets/cpcb/processed/cpcb_pm25_daily.csv"
df_daily.to_csv(output_path, index=False)

print(f"✅ Cleaned PM2.5 saved at: {output_path}")
