# 🔌 Electric Vehicle Population Analysis

A data-driven exploratory analysis of electric vehicle registrations to uncover trends, distributions, and adoption patterns across counties, fuel eligibility types, and more.

---

## 📁 Project Structure

```
electric-vehicle-eda/
│
├── data/                          # Raw dataset (CSV)
│   └── Electric_Vehicle_Population_Data.csv
│
├── notebooks/
│   └── eda_visualization.ipynb   # Original notebook version
│
├── src/                          # Modular Python scripts
│   ├── data_loader.py
│   ├── preprocess.py
│   └── plot_generator.py
│
├── main.py                       # Main entry point for analysis
├── requirements.txt              # Python dependencies
├── .gitignore
└── README.md
```

---

## 📌 Dataset Information

- **Source**: Washington State Department of Licensing  
- **Description**: Contains data on electric vehicles, including type, make, year, range, location, eligibility status, and utility provider.

---

## 📊 Key Insights & Visuals

- Distribution of Electric Vehicle Types (Bar & Pie)
- Top 10 Counties by EV Count
- Year-wise EV Manufacturing Trend
- CAFV (Clean Alternative Fuel Vehicle) Eligibility Analysis
- Electric Range Distribution (Histogram)
- EV Count by Electric Utility Providers

---

## 🛠️ Technologies Used

- `Python`
- `Pandas`
- `NumPy`
- `Matplotlib`
- `Seaborn`

---

## 🚀 Getting Started

### ✅ Installation

1. Clone the repository:
```bash
git clone https://github.com/Ankith-55/ev-population_eda.git
cd ev-population_eda
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the analysis:
```bash
python main.py
```

---

## 🧹 Preprocessing Summary

- Dropped irrelevant columns (e.g., VIN, Vehicle Location, DOL Vehicle ID)
- Removed null entries in selected fields
- Cleaned column names

---

## 📌 Future Work

- Add predictive modeling (e.g., vehicle adoption forecasting)
- Build an interactive Streamlit dashboard
- Add geospatial heatmaps for EV concentration

---

## 👨‍💻 Author

**Ankith V** – B.Tech AI & Data Science @ SNU Chennai  
Feel free to connect on [LinkedIn](https://www.linkedin.com/in/ankith-vijayyan/) 

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
