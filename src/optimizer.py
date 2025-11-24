import pandas as pd
import numpy as np
from pypfopt import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns
try:
    from src.data_loader import load_sp500_stocks
except ImportError:
    from data_loader import load_sp500_stocks

def optimize_portfolio(tickers, start_date='2020-01-01'):
    """
    Optimizes a portfolio for a given list of tickers.
    
    Args:
        tickers (list): List of ticker symbols.
        start_date (str): Start date for historical data.
        
    Returns:
        weights (dict): Optimized asset weights.
        performance (tuple): (Expected Return, Volatility, Sharpe Ratio)
    """
    print(f"Optimizing portfolio for: {tickers}")
    
    import yfinance as yf
    
    # Download data from yfinance
    try:
        df_all = yf.download(tickers, start=start_date)['Close']
    except Exception as e:
        print(f"Error downloading data: {e}")
        return None, None
    
    # If only one ticker, it returns a Series, convert to DataFrame
    if isinstance(df_all, pd.Series):
        df_all = df_all.to_frame()
        
    # Drop columns with all NaNs
    prices = df_all.dropna(axis=1, how='all')
    
    # Fill remaining missing values (forward fill then backward fill)
    prices = prices.ffill().bfill()
    
    if prices.empty:
        print("No data found for the specified tickers/date range.")
        return None, None

    # Calculate expected returns and sample covariance
    mu = expected_returns.mean_historical_return(prices)
    S = risk_models.sample_cov(prices)

    # Optimize for maximal Sharpe ratio
    ef = EfficientFrontier(mu, S)
    weights = ef.max_sharpe()
    cleaned_weights = ef.clean_weights()
    
    performance = ef.portfolio_performance(verbose=True)
    
    return cleaned_weights, performance

if __name__ == "__main__":
    # Test with a few tech stocks
    test_tickers = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA']
    weights, perf = optimize_portfolio(test_tickers)
    print("Optimized Weights:", weights)
