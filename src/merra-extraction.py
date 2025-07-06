import xarray as xr
import pandas as pd
from pathlib import Path

# Where .nc4 files are (downloaded ones)
data_dir = Path("datasets/merra")

# Where to save processed CSVs
output_dir = Path("datasets/merra-outputs-csv")
output_dir.mkdir(parents=True, exist_ok=True)


# List all .nc4 files
nc_files = sorted(data_dir.glob("*.nc4"))

for file_path in nc_files:
    print(f"Processing {file_path.name}...")

    try:
        ds = xr.open_dataset(file_path)

        # Extract variables
        bc = ds["BCSMASS"].squeeze()
        dust = ds["DUSMASS25"].squeeze()
        oc = ds["OCSMASS"].squeeze()
        so4 = ds["SO4SMASS"].squeeze()
        ss = ds["SSSMASS25"].squeeze()

        # Combine all to approximate PM2.5
        pm25 = bc + dust + oc + so4 + ss

        # Convert to DataFrame
        df = pm25.to_dataframe(name="PM25_components").reset_index()

        # Filter India (approx. bounding box)
        df_india = df[
            (df["lat"] >= 5) & (df["lat"] <= 35) &
            (df["lon"] >= 65) & (df["lon"] <= 95)
        ]

        # Extract timestamp from file name
        month_str = file_path.stem.split(".")[-1]  # example: '202001'

        # Save CSV
        df_india.to_csv(output_dir / f"pm25_{month_str}.csv", index=False)
        print(f"Saved: pm25_{month_str}.csv")

    except Exception as e:
        print(f"Error processing {file_path.name}: {e}")
