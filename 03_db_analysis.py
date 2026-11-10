import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def analyze_and_plot():
    conn = sqlite3.connect('data/tallinn_mobility.db')
    
    query = """
    SELECT 
        CAST(strftime('%H', timestamp) AS INTEGER) AS hour_of_day,
        ROUND(AVG(net_fare_eur), 2) AS avg_net_fare,
        COUNT(*) AS total_rides
    FROM rides
    GROUP BY hour_of_day
    ORDER BY hour_of_day;
    """
    
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    plt.figure(figsize=(10, 5))
    plt.plot(df['hour_of_day'], df['avg_net_fare'], marker='o', color='#1f77b4', linewidth=2)
    plt.title('Tallinn Ride-Hailing: Hourly Driver Revenue (SQL Query Driven)', fontsize=12, fontweight='bold')
    plt.xlabel('Hour of Day (0-23)', fontsize=10)
    plt.ylabel('Avg Revenue per Hour (€)', fontsize=10)
    plt.xticks(range(0, 24))
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    
    output_path = 'hourly_revenue_from_db.png'
    plt.savefig(output_path, dpi=300)
    print(f"Analysis chart saved as {output_path}")

if __name__ == '__main__':
    analyze_and_plot()
