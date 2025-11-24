import pandas as pd
from prophet import Prophet
import os
try:
    from src.data_loader import load_sp500_index
except ImportError:
    from data_loader import load_sp500_index

def train_forecast_model(periods=365):
    """
    Trains a Prophet model on the S&P 500 index and forecasts future prices.
    
    Args:
        periods (int): Number of days to forecast.
        
    Returns:
        model (Prophet): Trained Prophet model.
        forecast (pd.DataFrame): Forecast dataframe.
    """
    print("Loading data for forecasting...")
    df = load_sp500_index()
    
    # Prepare data for Prophet (ds, y)
    df_prophet = df[['Date', 'S&P500']].rename(columns={'Date': 'ds', 'S&P500': 'y'})
    
    print("Training Prophet model...")
    m = Prophet(daily_seasonality=True)
    m.fit(df_prophet)
    
    print(f"Forecasting for {periods} days...")
    future = m.make_future_dataframe(periods=periods)
    forecast = m.predict(future)
    
    return m, forecast

if __name__ == "__main__":
    model, forecast = train_forecast_model(periods=30)
    print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())
    
    # Save forecast plot
    output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'notebooks')
    fig1 = model.plot(forecast)
    fig1.savefig(os.path.join(output_dir, 'prophet_forecast.png'))
    print("Saved prophet_forecast.png")
