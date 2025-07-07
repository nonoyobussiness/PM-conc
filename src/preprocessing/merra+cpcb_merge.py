import pandas as pd
import numpy as np
from scipy.spatial import cKDTree
import os

# Load CPCB data
cpcb = pd.read_csv("datasets/cpcb/processed/cpcb_pm25_daily.csv", parse_dates=["date"])
cpcb = cpcb.dropna(subset=["Latitude", "Longitude"])

# Extract 'year-month' for monthly merge
cpcb["year_month"] = cpcb["date"].dt.strftime("%Y%m")

merged_rows = []

for i, row in cpcb.iterrows():
    year_month = row["year_month"]
    merra_path = f"datasets/merra/merra_processed/pm25_{year_month}.csv"

    print(f"\n🔎 Processing row {i}: Month = {year_month} | City = {row['City']}")

    if not os.path.exists(merra_path):
        print(f"❌ No MERRA file for {year_month}")
        continue

    # Load monthly MERRA data
    merra = pd.read_csv(merra_path)
    if merra.empty:
        print(f"⚠️ Empty MERRA data for {year_month}")
        continue

    # Nearest spatial match (lat, lon)
    tree = cKDTree(merra[["lat", "lon"]].values)
    dist, idx = tree.query([row["Latitude"], row["Longitude"]])
    nearest_row = merra.iloc[idx]

    combined_row = {
        **row.to_dict(),
        "PM25_MERRA": nearest_row["PM25_components"]
    }
    merged_rows.append(combined_row)

# Final merge output
merged_df = pd.DataFrame(merged_rows)
output_path = "datasets/cpcb+merra_processed/merged_model_input_monthly.csv"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
merged_df.to_csv(output_path, index=False)

print(f"\n✅ Monthly MERRA-CPCB merged data saved at: {output_path}")
