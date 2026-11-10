import os
import sqlite3
import pandas as pd

def setup_db():
    csv_path = 'data/raw_rides_data.csv'
    db_path = 'data/tallinn_mobility.db'
    
    if not os.path.exists(csv_path):
        print("Raw data missing. Please run 01_generate_data.py first.")
        return
        
    df = pd.read_csv(csv_path)
    conn = sqlite3.connect(db_path)
    
    df.to_sql('rides', conn, if_exists='replace', index=False)
    conn.close()
    print(f"Data successfully imported into SQLite database: {db_path}")

if __name__ == '__main__':
    setup_db()
