## 📌 PM2.5 Estimation Using Satellite & Reanalysis Data

### 🔬 Overview

This project aims to **predict surface-level PM2.5 concentrations across India** using:

- 🚀 **Satellite-derived AOD** _(INSAT-3D/3DR/3DS - pending access)_
- 🌫️ **MERRA-2 aerosol reanalysis** _(BC, SO4, OC, Dust, Sea Salt)_
- ☁️ **Meteorological variables** _(PBL Height, Cloud Fraction – from NICES)_
- 🧠 **AI/ML Models** _(Random Forest, XGBoost, CatBoost)_
- 📍 **Ground truth from CPCB monitoring stations**

It is part of our solution to the [ISRO Bhuvan Atmospheric Hackathon 2025](https://bhuvan-app1.nrsc.gov.in/isrohackathon2025/), focusing on **spatial pollution mapping** in areas with sparse sensors.

---

### 📁 Project Structure

```
PM-conc/
│
├── datasets/
│   ├── cpcb/
│   │   ├── PM2.5/             # Raw CPCB CSVs per city/year
│   │   ├── city_coordinates.csv  # Lat/Lon for major cities
│   │   └── processed/         # ✅ Output after running preprocessing script
│   │       └── cpcb_pm25_daily.csv
│   ├── merra/
│   │   ├── merra_unprocessed/ # Raw .nc4 files
│   │   └── merra_processed/   # ✅ Output after running extraction script
│   └── cpcb+merra_processed/  # ✅ Merged CPCB-MERRA
│
├── results/                   # Model outputs, metrics, plots
│
├── src/
│   └── preprocessing/
│       ├── cpcb_preprocessing.py
│       ├── merra_extraction.py
│       └── merra+cpcb_merge.py
│
├── notebooks/                 # Optional: Jupyter notebooks for modeling
├── .venv/
├── .gitignore
├── requirements.txt
└── README.md
```

---

### ⚙️ Setup Instructions

#### 1. Clone the repo

```bash
git clone https://github.com/your-username/PM-conc.git
cd PM-conc
```

#### 2. Set up virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

#### 3. Download MERRA-2 Data

Create a NASA EarthData account: [https://urs.earthdata.nasa.gov/](https://urs.earthdata.nasa.gov/)

Then run:

```bash
wget --load-cookies ~/.urs_cookies --save-cookies ~/.urs_cookies --keep-session-cookies \
     --user YOUR_USERNAME --password YOUR_PASSWORD \
     -i datasets/merra/merra-links.txt -P datasets/merra/merra_unprocessed
```

#### 4. Run MERRA Extraction

```bash
python src/preprocessing/merra_extraction.py
```

#### 5. Run CPCB Preprocessing

```bash
python src/preprocessing/cpcb_preprocessing.py
```

#### 6. Merge MERRA & CPCB Data

```bash
python src/preprocessing/merra+cpcb_merge.py
```

This will generate `merged_model_input.csv` in `datasets/cpcb+merra_processed/`.

---

### 📊 Features Used

- **MERRA Variables**

  - `BCSMASS` - Black Carbon
  - `DUSMASS25` - Dust
  - `OCSMASS` - Organic Carbon
  - `SO4SMASS` - Sulfates
  - `SSSMASS25` - Sea Salt

- **CPCB PM2.5** (target variable)

- **Optional Features (from CPCB)**
  - `AT (°C)`, `RH (%)`, `WS`, `BP`, `RF` → weather

---

### ✅ Progress Summary

#### ✅ Done

- Downloaded & preprocessed MERRA-2 `.nc4` files for 2019–2023
- Extracted India-bounded PM2.5 approximation from MERRA
- Fetched CPCB PM2.5 (city-wise) and cleaned to daily format
- Structured data folder for modeling phase
- Merged CPCB and MERRA data with spatial and temporal matching
- Trained ML models: Random Forest, XGBoost, CatBoost
- Compared performance: MAE & R²

#### 🧠 In Progress

- Feature engineering with spatial/seasonal features
- Adding missing satellite AOD (INSAT)

#### 🧠 Planned Next

- Downscale MERRA spatial resolution (0.25° → ~5 km grid)
- Add temporal lag features
- Visualize predictions using heatmaps or Folium maps

---

### ⚠️ TODO

- Build interactive dashboard for visualizations
- Integrate INSAT AOD pipeline
- Incorporate station-wise validation metrics

---

### 📌 References

- [MERRA-2 Aerosol Dataset](https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/)
- [GES DISC Access Guide](https://disc.gsfc.nasa.gov/)
- [CPCB PM2.5 Data](https://app.cpcbccr.com/ccr/#/caaqm-dashboard/all-caaqm-data)
- [ISRO Hackathon Portal](https://bhuvan-app1.nrsc.gov.in/isrohackathon2025/)

---

### 🦆‍♂️ Contributors

- **Sree Vathsal**
- **Hrishikesh Reddy**
- **Tathya Sharma**
