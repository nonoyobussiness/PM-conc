📌 PM2.5 Estimation Using Satellite & Reanalysis Data
🔬 Overview
This project aims to predict surface-level PM2.5 concentrations across India using:

🚀 Satellite-derived AOD (INSAT-3D/3DR/3DS - pending access)

🌫️ MERRA-2 aerosol reanalysis (BC, SO4, OC, Dust, Sea Salt)

🌥️ Meteorological variables (PBL Height, Cloud Fraction – from NICES)

🧠 AI/ML Models (Random Forest, XGBoost, CatBoost)

📍 Ground truth from CPCB monitoring stations

It is part of our solution to the ISRO Bhuvan Atmospheric Hackathon 2025, focusing on spatial pollution mapping in areas with sparse sensors.

📁 Project Structure
graphql
Copy
Edit
PM-conc/
│
├── datasets/
│ ├── cpcb/
│ │ ├── PM2.5/ # Raw CPCB CSVs per city/year
│ │ ├── city_coordinates.csv # Lat/Lon for major cities
│ │ └── processed/ # ✅ Output after running preprocessing script
│ │ └── cpcb_pm25_daily.csv
│ ├── merra/
│ │ ├── merra_unprocessed/ # Raw .nc4 files
│ │ └── merra_processed/ # ✅ Output after running extraction script
│ └── cpcb+merra_processed/ # ✅ Merged CPCB-MERRA
│
├── results/ # Model outputs, metrics, plots
│
├── src/
│ └── preprocessing/
│ ├── cpcb_preprocessing.py
│ ├── merra_extraction.py
│ └── merra+cpcb_merge.py
│
├── notebooks/ # Optional: Jupyter notebooks for modeling
├── .venv/
├── .gitignore
├── requirements.txt
└── README.md
⚙️ Setup Instructions

1. Clone the repo
   bash
   Copy
   Edit
   git clone https://github.com/your-username/PM-conc.git
   cd PM-conc
2. Set up virtual environment
   bash
   Copy
   Edit
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
3. Download MERRA-2 Data
   Create a NASA EarthData account: https://urs.earthdata.nasa.gov/

Then run:

bash
Copy
Edit
wget --load-cookies ~/.urs_cookies --save-cookies ~/.urs_cookies --keep-session-cookies \
 --user YOUR_USERNAME --password YOUR_PASSWORD \
 -i datasets/merra/merra-links.txt -P datasets/merra/merra_unprocessed 4. Run MERRA Extraction
bash
Copy
Edit
python src/preprocessing/merra_extraction.py 5. Run CPCB Preprocessing
bash
Copy
Edit
python src/preprocessing/cpcb_preprocessing.py 6. Merge MERRA & CPCB Data
bash
Copy
Edit
python src/preprocessing/merra+cpcb_merge.py
This will generate merged_model_input.csv in datasets/cpcb+merra_processed/.

📊 Features Used
🌀 MERRA Aerosol Components
BCSMASS – Black Carbon

DUSMASS25 – Dust (PM2.5 fraction)

OCSMASS – Organic Carbon

SO4SMASS – Sulfates

SSSMASS25 – Sea Salt (PM2.5 fraction)

🌤️ Meteorology (Planned)
PBL Height

Cloud Fraction

Wind Speed, Temperature, RH

📍 Spatial + Temporal
Nearest MERRA grid point to CPCB station

Day of Week, Month

Season (Winter, Summer, Monsoon, Post-Monsoon) → One-hot encoded

✅ Model Results
We trained multiple ML models using MERRA + CPCB merged features:

🔍 Random Forest
MAE: 29.33

R²: -0.27

🔍 XGBoost
MAE: 29.24

R²: -0.08

🔍 CatBoost
MAE: 28.13

R²: -0.11

Despite low scores, this confirms PM2.5_MERRA provides a weak but usable signal.
Future improvement will involve including AOD, PBLH, and cloud cover.

📈 Feature Importance (CatBoost)
Feature Importance
PM2.5_MERRA ✅ Highest
Month / Season Moderate
DayOfWeek Minor

📍 Next Steps
🔁 Impute missing AOD using MERRA met features

📈 Train improved models using AOD + weather + PM2.5_MERRA

🌐 Generate high-resolution PM2.5 maps

🧪 Spatial cross-validation & temporal smoothing

📊 Build interactive dashboard

📌 References
MERRA-2 Aerosol Dataset

GES DISC Access Guide

CPCB PM2.5 Data

ISRO Hackathon Portal

🦆‍♂️ Contributors
Sree Vathsal

Hrishikesh Reddy

Tathya Sharma
