import os
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def generate_rides():
    np.random.seed(42)
    n_records = 5000
    
    start_date = datetime(2026, 1, 1)
    dates = [start_date + timedelta(days=np.random.randint(0, 310), 
                                      hours=np.random.randint(0, 24), 
                                      minutes=np.random.randint(0, 60)) for _ in range(n_records)]
    
    neighborhoods = ['Kesklinn', 'Vanalinn', 'Lasnamäe', 'Mustamäe', 'Kristiine', 'Põhja-Tallinn', 'Nõmme', 'Haabersti']
    weights = [0.25, 0.15, 0.20, 0.12, 0.08, 0.10, 0.05, 0.05]
    
    pickup_locations = np.random.choice(neighborhoods, size=n_records, p=weights)
    
    fares = []
    durations = []
    
    for dt, loc in zip(dates, pickup_locations):
        weekday = dt.weekday()
        hour = dt.hour
        
        if weekday in [4, 5]: # Fri, Sat
            base_fare = np.random.normal(7.8, 2.6)
        else: # Mon-Thu target ~13€/h net
            base_fare = np.random.normal(5.0, 1.6)
            
        if loc in ['Kesklinn', 'Vanalinn']:
            base_fare += 1.5
            
        if 0 <= hour <= 5: # Night time: higher unit price, lower volume
            base_fare += 2.2
            
        fare = max(2.5, round(base_fare, 2))
        fares.append(fare)
        
        duration = int(np.clip(fare * np.random.uniform(1.8, 2.5), 4, 45))
        durations.append(duration)
        
    df = pd.DataFrame({
        'ride_id': [f"RIDE_{1000+i}" for i in range(n_records)],
        'timestamp': [dt.strftime('%Y-%m-%d %H:%M:%S') for dt in dates],
        'neighborhood': pickup_locations,
        'fare_eur': fares,
        'duration_mins': durations,
        'commission_rate': 0.20
    })
    
    df['net_fare_eur'] = round(df['fare_eur'] * (1 - df['commission_rate']), 2)
    
    os.makedirs('data', exist_ok=True)
    file_path = 'data/raw_rides_data.csv'
    df.to_csv(file_path, index=False)
    print(f"Simulated dataset generated at {file_path}")

if __name__ == '__main__':
    generate_rides()
