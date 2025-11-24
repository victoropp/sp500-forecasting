import pandas as pd
import os

# Define paths
# Define paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

def load_sp500_index():
    """Loads the S&P 500 index data."""
    path = os.path.join(DATA_DIR, 'sp500_index.csv')
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
    return df

def load_sp500_companies():
    """Loads the S&P 500 companies data."""
    path = os.path.join(DATA_DIR, 'sp500_companies.csv')
    df = pd.read_csv(path)
    return df

def load_sp500_stocks():
    """Loads the S&P 500 stocks data."""
    path = os.path.join(DATA_DIR, 'sp500_stocks.csv')
    # This file is large, so we might want to optimize loading or load specific columns
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

if __name__ == "__main__":
    # Test loading
    print("Loading Index...")
    index = load_sp500_index()
    print(f"Index shape: {index.shape}")
    print(index.head())
    
    print("\nLoading Companies...")
    companies = load_sp500_companies()
    print(f"Companies shape: {companies.shape}")
    print(companies.head())
