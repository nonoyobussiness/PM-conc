## 📌 PM2.5 Estimation Using Satellite & Reanalysis Data

### 🔬 Overview

This project aims to **predict surface-level PM2.5 concentrations across India** using:

- 🚀 **Satellite-derived AOD**
- 🌫️ **MERRA-2 aerosol reanalysis (BC, SO4, OC, Dust, Sea Salt)**
- 🧠 **AI/ML Models**
- 📍 **Ground truth from CPCB monitoring stations**

It is part of our solution to the [ISRO Bhuvan Atmospheric Hackathon 2025](https://bhuvan-app1.nrsc.gov.in/isrohackathon2025/), focusing on **spatial pollution mapping** in areas with sparse sensors.

---

### 📁 Project Structure

```
PM-conc/
│
├── datasets/
│   ├── merra/              # Downloaded .nc4 files
│   ├── cpcb/               # Ground-truth PM2.5 CSVs from CPCB
│   └── merra-links.txt     # List of .nc4 URLs (NASA GES DISC)
│
├── outputs/
│   └── merra/              # Extracted CSVs with PM2.5 estimates
│
├── src/
│   ├── merra_extraction.py # Script to convert .nc4 to CSV
│   ├── modeling.py         # (Planned) ML model training
│   └── utils.py            # (Planned) Helper functions
│
├── .venv/                  # Python virtual environment
├── requirements.txt        # Required Python packages
└── README.md               # You're reading it
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
     -i datasets/merra-links.txt -P datasets/merra/
```

#### 4. Run MERRA Extraction

```bash
python src/merra_extraction.py
```

This will generate PM2.5 estimates for India in `outputs/merra/`.

---

### 📊 Features Used

- **BCSMASS** - Black Carbon
- **DUSMASS25** - Fine Dust Particles
- **OCSMASS** - Organic Carbon
- **SO4SMASS** - Sulfates
- **SSSMASS25** - Sea Salt

PM2.5 is approximated by summing these.

---

### ⚠️ TODO

- [x] Download and preprocess MERRA-2
- [x] Extract India-only PM2.5 approximations
- [ ] Integrate CPCB ground station data
- [ ] Build ML regression model (XGBoost, LSTM, etc.)
- [ ] Visualize spatial PM2.5 estimates (via Folium/Plotly)

---

### 📌 References

- [MERRA-2 Aerosol Dataset](https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/)
- [GES DISC Access Guide](https://disc.gsfc.nasa.gov/)
- [CPCB PM2.5 Data](https://app.cpcbccr.com/ccr/#/caaqm-dashboard/all-caaqm-data)

---

### 🙆‍♂️ Contributors

- **Sree Vathsal** — Project Lead, Data Pipeline
- You can add your teammates here too.
