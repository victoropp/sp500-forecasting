import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from data_loader import load_sp500_index, load_sp500_companies

# Setup output directory
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'notebooks')
os.makedirs(OUTPUT_DIR, exist_ok=True)

def run_eda():
    print("Running EDA...")
    
    # 1. S&P 500 Index Trend
    df_index = load_sp500_index()
    
    plt.figure(figsize=(12, 6))
    plt.plot(df_index['Date'], df_index['S&P500'], label='S&P 500')
    plt.title('S&P 500 Index Historical Performance')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(OUTPUT_DIR, 'sp500_trend.png'))
    plt.close()
    print("Saved sp500_trend.png")
    
    # 2. Sector Distribution
    df_companies = load_sp500_companies()
    
    plt.figure(figsize=(10, 6))
    sector_counts = df_companies['Sector'].value_counts()
    sns.barplot(x=sector_counts.values, y=sector_counts.index, palette='viridis')
    plt.title('S&P 500 Sector Distribution')
    plt.xlabel('Number of Companies')
    plt.savefig(os.path.join(OUTPUT_DIR, 'sector_distribution.png'))
    plt.close()
    print("Saved sector_distribution.png")
    
    # 3. Top 10 Companies by Market Cap
    plt.figure(figsize=(10, 6))
    top_10 = df_companies.nlargest(10, 'Marketcap')
    sns.barplot(x='Marketcap', y='Shortname', data=top_10, palette='magma')
    plt.title('Top 10 S&P 500 Companies by Market Cap')
    plt.xlabel('Market Cap')
    plt.savefig(os.path.join(OUTPUT_DIR, 'top_10_market_cap.png'))
    plt.close()
    print("Saved top_10_market_cap.png")

if __name__ == "__main__":
    run_eda()
