## 📌 PM2.5 Estimation Using Satellite & Reanalysis Data

### 🔬 Overview

This project aims to **predict surface-level PM2.5 concentrations across India** using:

- 🚀 **Satellite-derived AOD** _(INSAT-3D/3DR/3DS - pending access)_
- 🌫️ **MERRA-2 aerosol reanalysis** _(BC, SO4, OC, Dust, Sea Salt)_
- 🌥️ **Meteorological variables** _(PBL Height, Temperature, RH, Wind, etc.)_
- 🧠 **AI/ML Models** _(Random Forest, XGBoost, Imputation)_
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
│   │   └── processed/         # ✅ Output after running preprocessing script
│   │       └── cpcb_pm25_daily.csv  # ❗ Not versioned – generated locally
│   ├── merra/                 # MERRA .nc4 files
│   └── pblh/                  # (Planned) PBLH & Cloud Fraction datasets
│
├── results/                   # Model outputs, metrics, plots
│
├── src/
│   └── preprocessing/
│       ├── cpcb-preprocessing.py   # Extracts daily PM2.5 from raw CPCB
│       └── merra-extraction.py     # Converts .nc4 to PM2.5 CSVs
│
├── .venv/                     # Python virtual environment
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

This will generate daily PM2.5 ground truth in `datasets/cpcb/processed/cpcb_pm25_daily.csv`.

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

#### 🧠 In Progress

- Merging MERRA & CPCB data by **date and nearest location**
- Handling mismatches in date format and timezones

#### 🧠 Planned Next

- Impute missing AOD using MERRA met features
- Train regression model (Random Forest / XGBoost)
- Downscale MERRA spatial resolution (0.25° → \~5 km grid)
- Visualize outputs using Folium or heatmap layers

---

### ⚠️ TODO

- ***

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
