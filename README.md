# 📈 S&P 500 Intelligent Forecasting & Portfolio Optimizer

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B)](https://streamlit.io/)
[![Prophet](https://img.shields.io/badge/Prophet-Time%20Series-00D9FF)](https://facebook.github.io/prophet/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **Advanced Financial Analytics Platform** combining time series forecasting with Modern Portfolio Theory for S&P 500 prediction and optimal asset allocation. Interactive dashboard with Meta's Prophet and PyPortfolioOpt.

---

## 🎯 Project Overview

A state-of-the-art **quantitative finance** platform demonstrating:

- 📊 **Time Series Forecasting**: Meta's Prophet model for S&P 500 predictions
- 💼 **Portfolio Optimization**: Modern Portfolio Theory (MPT) implementation
- 📈 **Efficient Frontier**: Risk-return optimization with Sharpe ratio maximization
- 🎨 **Interactive Dashboard**: Premium financial terminal built with Streamlit
- 📉 **Risk Analytics**: Volatility analysis, confidence intervals, and backtesting

### Key Features
- ✅ **Prophet forecasting** with 90-day S&P 500 predictions
- ✅ **Efficient Frontier** visualization for optimal portfolios
- ✅ **Max Sharpe Ratio** portfolio allocation
- ✅ **Interactive dashboard** with real-time data
- ✅ **Risk metrics** (volatility, returns, Sharpe ratio)

---

## 🚀 Features

### 1. 📊 Market Forecasting
- **Prophet Model**: Facebook's robust time series forecasting
- **Confidence Intervals**: Upper and lower bounds for predictions
- **90-Day Horizon**: Future S&P 500 price predictions
- **Trend Analysis**: Seasonality and trend decomposition
- **Historical Performance**: Backtesting against actual data

### 2. 💼 Portfolio Optimization
- **Modern Portfolio Theory**: Markowitz optimization framework
- **Efficient Frontier**: Risk-return tradeoff visualization
- **Max Sharpe Ratio**: Optimal portfolio allocation
- **Multi-Asset**: S&P 500 constituent optimization
- **Risk Analysis**: Volatility, expected returns, correlation matrices

### 3. 🎨 Interactive Dashboard
- **Premium UI**: Dark theme financial terminal
- **Real-Time Data**: Live S&P 500 data integration
- **Interactive Charts**: Plotly-based visualizations
- **Multi-Tab Interface**: Forecasting, optimization, analytics
- **Downloadable Results**: Export predictions and allocations

---

## 📊 Model Performance

### Prophet Forecasting
- **Model**: Meta's Prophet (Additive time series model)
- **Features**: Trend, yearly/weekly seasonality
- **Horizon**: 90 days
- **Uncertainty**: 80% confidence intervals
- **Historical Data**: ~1 year of S&P 500 daily prices

### Portfolio Optimization
- **Method**: Mean-variance optimization (Markowitz)
- **Objective**: Maximize Sharpe ratio
- **Constraints**: Weights sum to 1.0, no short selling
- **Risk-Free Rate**: Configurable (default: 2% annually)
- **Rebalancing**: Quarterly recommended

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────┐
│         Yahoo Finance API (yfinance)            │
│        S&P 500 Index & Constituents             │
└────────────────┬────────────────────────────────┘
                 │
    ┌────────────┴────────────┐
    │                         │
┌───▼──────────┐    ┌────────▼─────────┐
│ Prophet      │    │  PyPortfolioOpt  │
│ Forecasting  │    │  Optimization    │
│ • Trend      │    │  • MPT           │
│ • Seasonality│    │  • Sharpe Ratio  │
│ • Confidence │    │  • Efficient     │
│   Intervals  │    │    Frontier      │
└───┬──────────┘    └────────┬─────────┘
    │                        │
    └────────────┬───────────┘
                 │
        ┌────────▼─────────┐
        │  Data Processing │
        │  • Price data    │
        │  • Returns calc  │
        │  • Correlation   │
        └────────┬─────────┘
                 │
        ┌────────▼─────────┐
        │  Streamlit UI    │
        │  • Forecasting   │
        │  • Optimization  │
        │  • Analytics     │
        └──────────────────┘
```

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Internet connection (for data download)

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/sp500-forecasting.git
cd sp500_forecasting
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the dashboard**
```bash
streamlit run deployment/app.py
```

The dashboard will open at `http://localhost:8501`

---

## 🚀 Quick Start

### Option 1: Run the Dashboard (Recommended)

```bash
streamlit run deployment/app.py
```

Navigate through the tabs:
- **📈 Forecast**: View S&P 500 predictions
- **💼 Portfolio**: Optimize asset allocation
- **📊 Analytics**: Explore market insights

### Option 2: Use as Python Library

```python
from src.data_loader import load_sp500_index, load_sp500_companies
from src.forecaster import train_forecast_model
from src.optimizer import optimize_portfolio

# Load data
sp500_data = load_sp500_index(period='1y')

# Forecast
forecast = train_forecast_model(sp500_data, periods=90)

# Optimize portfolio
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA']
weights, metrics = optimize_portfolio(tickers, period='1y')

print(f"Expected Return: {metrics['expected_return']:.2%}")
print(f"Volatility: {metrics['volatility']:.2%}")
print(f"Sharpe Ratio: {metrics['sharpe_ratio']:.2f}")
```

---

## 📊 Dataset

**Source**: Yahoo Finance (via yfinance API)

### S&P 500 Index Data
- **Ticker**: ^GSPC
- **Period**: 1+ years of historical data
- **Frequency**: Daily closing prices
- **Features**: Open, High, Low, Close, Volume
- **Updates**: Real-time via API

### S&P 500 Constituents
- **Total**: 503 companies (as of dataset)
- **Sectors**: Technology, Healthcare, Finance, Consumer, etc.
- **Data**: Historical prices for portfolio optimization
- **Rebalancing**: Quarterly recommended

---

## 🛠️ Technology Stack

### Time Series Forecasting
- **Prophet**: Meta's additive time series model
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing

### Portfolio Optimization
- **PyPortfolioOpt**: Modern Portfolio Theory implementation
- **CVXPY**: Convex optimization
- **Scikit-learn**: Risk metrics and preprocessing

### Visualization & Deployment
- **Streamlit**: Interactive web application
- **Plotly**: Dynamic financial charts
- **Matplotlib/Seaborn**: Static visualizations

### Data Acquisition
- **yfinance**: Yahoo Finance API wrapper
- **Real-time data**: Live market data integration

---

## 📁 Project Structure

```
sp500_forecasting/
├── src/
│   ├── data_loader.py          # Yahoo Finance data retrieval
│   ├── forecaster.py           # Prophet model training
│   ├── optimizer.py            # MPT portfolio optimization
│   └── eda.py                  # Exploratory data analysis
├── deployment/
│   └── app.py                  # Streamlit dashboard
├── data/
│   ├── sp500_index.csv         # Historical S&P 500 data
│   └── sp500_companies.csv     # Constituent company data
├── notebooks/                  # Jupyter notebooks (optional)
├── social_media/               # Graphics for sharing
├── requirements.txt            # Python dependencies
├── LICENSE                     # MIT License
└── README.md                   # This file
```

---

## 🎓 Key Learnings & Skills Demonstrated

### Quantitative Finance
- ✅ Modern Portfolio Theory (Markowitz optimization)
- ✅ Efficient Frontier construction
- ✅ Sharpe ratio maximization
- ✅ Risk-return tradeoff analysis
- ✅ Portfolio rebalancing strategies

### Time Series Analysis
- ✅ Prophet model implementation
- ✅ Trend and seasonality decomposition
- ✅ Forecasting with confidence intervals
- ✅ Model validation and backtesting

### Software Engineering
- ✅ Modular code architecture
- ✅ Interactive dashboard development
- ✅ Real-time data integration
- ✅ Production-ready deployment

### Financial Analytics
- ✅ Market data acquisition (Yahoo Finance)
- ✅ Returns and volatility calculation
- ✅ Correlation matrix analysis
- ✅ Risk metrics computation

---

## 🚀 Usage Examples

### Forecast S&P 500

```python
from src.data_loader import load_sp500_index
from src.forecaster import train_forecast_model

# Load historical data
data = load_sp500_index(period='2y')

# Train Prophet model
forecast = train_forecast_model(data, periods=90)

# View predictions
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())
```

### Optimize Portfolio

```python
from src.optimizer import optimize_portfolio

# Define portfolio
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'JPM', 'V']

# Optimize
weights, metrics = optimize_portfolio(
    tickers,
    period='1y',
    risk_free_rate=0.02
)

# View allocation
for ticker, weight in zip(tickers, weights):
    print(f"{ticker}: {weight:.2%}")

print(f"\nExpected Annual Return: {metrics['expected_return']:.2%}")
print(f"Annual Volatility: {metrics['volatility']:.2%}")
print(f"Sharpe Ratio: {metrics['sharpe_ratio']:.2f}")
```

### Generate Efficient Frontier

```python
from src.optimizer import generate_efficient_frontier

# Generate frontier
frontier_returns, frontier_volatilities = generate_efficient_frontier(
    tickers=['AAPL', 'MSFT', 'GOOGL', 'AMZN'],
    period='1y'
)

# Plot
import matplotlib.pyplot as plt
plt.plot(frontier_volatilities, frontier_returns)
plt.xlabel('Volatility (Risk)')
plt.ylabel('Expected Return')
plt.title('Efficient Frontier')
plt.show()
```

---

## 💡 Business Applications

### 1. 📊 Wealth Management
- **Portfolio Construction**: Build optimal portfolios for clients
- **Risk Management**: Quantify and manage portfolio risk
- **Rebalancing**: Maintain optimal allocation over time
- **Performance Reporting**: Track portfolio performance vs benchmark

### 2. 🏦 Institutional Investing
- **Asset Allocation**: Optimize across asset classes
- **Risk Budgeting**: Allocate risk efficiently
- **Benchmarking**: Compare against S&P 500 index
- **Scenario Analysis**: Stress testing and what-if scenarios

### 3. 🎯 Algorithmic Trading
- **Signal Generation**: Forecasts as trading signals
- **Portfolio Optimization**: Dynamic rebalancing
- **Risk Controls**: Volatility targeting
- **Backtesting**: Historical performance validation

### 4. 📈 Market Research
- **Trend Analysis**: Identify market trends
- **Seasonality**: Detect seasonal patterns
- **Volatility Forecasting**: Predict market turbulence
- **Correlation Analysis**: Understand asset relationships

---

## 📈 Future Enhancements

- [ ] Add more forecasting models (LSTM, ARIMA, XGBoost)
- [ ] Implement backtesting framework
- [ ] Add sector rotation strategies
- [ ] Include alternative assets (crypto, commodities)
- [ ] Real-time portfolio tracking
- [ ] Risk parity optimization
- [ ] Factor-based models (Fama-French)
- [ ] Monte Carlo simulations
- [ ] Machine learning for alpha generation
- [ ] RESTful API with FastAPI

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Victor Collins Oppon**
*Data Scientist | Quantitative Finance Specialist*

**Skills Showcased:**
- Time Series Forecasting (Prophet)
- Modern Portfolio Theory (MPT)
- Financial Analytics
- Interactive Dashboard Development
- Quantitative Research
- Risk Management

---

## 🙏 Acknowledgments

- Meta (Facebook) for Prophet
- Markowitz for Modern Portfolio Theory
- Yahoo Finance for market data
- Streamlit and Plotly teams

---

## ⚠️ Disclaimer

This project is for **educational and research purposes only**. It is **NOT financial advice**. The forecasts and portfolio recommendations are based on historical data and models that may not accurately predict future performance. Always consult with a qualified financial advisor before making investment decisions.

**Past performance does not guarantee future results.**

---

**⭐ If you find this project useful, please consider giving it a star!**

---

*Built with ❤️ by Victor Collins Oppon - Transforming data into intelligent investment insights*
