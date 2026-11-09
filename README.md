# 🚗 Tallinn Mobility & Driver Yield Optimization Analysis

An end-to-end data analytics project using Python, SQL, and SQLite to model ride-hailing dynamics, driver hourly yields, and demand distribution in Tallinn, Estonia.

## 📌 Project Overview
This project simulates and analyzes **5,000 ride-hailing transactions** in Tallinn, incorporating real-world market characteristics:
- Mon-Thu net hourly revenue baseline (~€13/hr after platform commission).
- Surge in weekend demand and overall earnings (Friday & Saturday).
- Higher per-trip fares during low-volume night shifts (00:00 - 05:00).

## 🛠 Tech Stack
- **Data Engineering**: Python (Pandas, NumPy)
- **Database**: SQLite
- **Analytics & SQL Queries**: SQLite SQL Engine
- **Visualization**: Matplotlib

## 📁 Repository Structure
```
tallinn-mobility-analysis/
├── data/
│   └── raw_rides_data.csv       # Generated 5k ride records
├── sql/
│   └── analytics_queries.sql    # Advanced SQL analytics script
├── src/
│   ├── 01_generate_data.py      # Data generation engine
│   ├── 02_setup_database.py     # SQLite ETL script
│   └── 03_db_analysis.py        # SQL execution & visualization
├── hourly_revenue_from_db.png   # Output chart
├── requirements.txt             # Project dependencies
└── README.md
```

## 🚀 How to Run
1. Clone repository:
   ```bash
   git clone https://github.com/musiclw88-cyber/tallinn-mobility-analysis.git
   cd tallinn-mobility-analysis
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run pipeline:
   ```bash
   python3 src/01_generate_data.py
   python3 src/02_setup_database.py
   python3 src/03_db_analysis.py
   ```
