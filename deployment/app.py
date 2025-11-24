import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import sys
import os

# Add project root to path to allow imports from src
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.data_loader import load_sp500_index, load_sp500_companies
from src.forecaster import train_forecast_model
from src.optimizer import optimize_portfolio

st.set_page_config(page_title="S&P 500 Intelligent Terminal", layout="wide", page_icon="📈")

# Custom CSS for premium look and high contrast
st.markdown("""
<style>
    /* Main Background and Text */
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    
    /* Headings */
    h1, h2, h3 {
        color: #00CC96 !important;
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    /* Metrics */
    [data-testid="stMetricValue"] {
        color: #00CC96 !important;
    }
    [data-testid="stMetricLabel"] {
        color: #e0e0e0 !important;
    }
    
    /* Buttons */
    .stButton > button {
        background-color: #262730;
        color: #ffffff !important;
        border: 1px solid #4c4c4c;
        border-radius: 5px;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #00CC96;
        color: #000000 !important;
        border-color: #00CC96;
    }
    
    /* Info Boxes */
    .stAlert {
        background-color: #262730;
        color: #ffffff;
        border: 1px solid #4c4c4c;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #0e1117;
        border-radius: 4px 4px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
        color: #ffffff;
    }
    .stTabs [aria-selected="true"] {
        background-color: #262730;
        color: #00CC96 !important;
        border-bottom: 2px solid #00CC96;
    }
    /* Widget Labels */
    .stSlider label, .stSelectbox label, .stMultiSelect label {
        color: #ffffff !important;
        font-size: 1.1rem !important;
        font-weight: bold !important;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar - Professional Profile
with st.sidebar:
    st.title("Victor Collins Oppon")
    st.markdown("**Data Scientist**")
    st.markdown("---")
    st.markdown("""
    **Expertise:**
    - 📈 Time Series Forecasting
    - 💼 Portfolio Optimization
    - 🤖 Machine Learning & AI
    - 📊 Financial Analytics
    """)
    st.markdown("---")
    st.markdown("""
    <div style='background-color: #262730; padding: 15px; border-radius: 5px; border: 1px solid #00CC96;'>
        <p style='color: #ffffff; margin: 0; font-weight: bold;'>
            This application demonstrates advanced financial modeling techniques including 
            <span style='color: #00CC96;'>Prophet</span> for forecasting and 
            <span style='color: #00CC96;'>Modern Portfolio Theory</span> for asset allocation.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.title("S&P 500 Analytics: Predictive Modeling & Portfolio Optimization")
st.markdown("""
<div style='background-color: #262730; padding: 15px; border-radius: 10px; border-left: 5px solid #00CC96;'>
    <h4 style='margin:0; color: #ffffff;'>Project Overview</h4>
    <p style='margin:0; color: #e0e0e0;'>
        This advanced data science platform integrates <b>Bayesian Time Series Forecasting</b> (Prophet) and 
        <b>Mean-Variance Optimization</b> (Modern Portfolio Theory) to deliver robust financial insights. 
        Designed for quantitative analysis, it enables probabilistic price projection and risk-adjusted asset allocation.
    </p>
</div>
<br>
""", unsafe_allow_html=True)

tabs = st.tabs(["🔮 Market Forecasting", "⚖️ Portfolio Optimizer", "📊 Stock Analysis"])

with tabs[0]:
    st.header("Market Overview & Forecasting")
    
    with st.expander("ℹ️ How this model works", expanded=False):
        st.markdown("""
        **Model:** Facebook Prophet
        
        **Methodology:** 
        Prophet is an additive regression model that fits non-linear trends with yearly, weekly, and daily seasonality, plus holiday effects. It works best with time series that have strong seasonal effects and several seasons of historical data.
        
        **Key Metrics:**
        - **Trend:** The underlying growth or decline.
        - **Seasonality:** Periodic fluctuations (e.g., market cycles).
        - **Uncertainty Intervals:** The shaded region represents the range of likely outcomes (80% confidence).
        """)
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.subheader("S&P 500 Price Prediction")
        days_to_forecast = st.slider("Select Forecast Horizon (Days)", 30, 365, 90)
        
        if st.button("Generate AI Forecast"):
            with st.spinner("Running Prophet Model..."):
                model, forecast = train_forecast_model(periods=days_to_forecast)
                
                # Plotly chart
                fig = go.Figure()
                
                # Historical data (last 2 years for visibility)
                historical = model.history.tail(730)
                fig.add_trace(go.Scatter(x=historical['ds'], y=historical['y'], mode='lines', name='Historical', line=dict(color='#00CC96')))
                
                # Forecast
                future_data = forecast.tail(days_to_forecast)
                fig.add_trace(go.Scatter(x=future_data['ds'], y=future_data['yhat'], mode='lines', name='Forecast', line=dict(color='#AB63FA', dash='dash')))
                fig.add_trace(go.Scatter(x=future_data['ds'], y=future_data['yhat_upper'], mode='lines', name='Upper Bound', line=dict(width=0), showlegend=False))
                fig.add_trace(go.Scatter(x=future_data['ds'], y=future_data['yhat_lower'], mode='lines', name='Lower Bound', fill='tonexty', line=dict(width=0), fillcolor='rgba(171, 99, 250, 0.2)', showlegend=False))
                
                fig.update_layout(
                    template="plotly_dark", 
                    height=500,
                    hovermode="x unified",
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    legend=dict(
                        font=dict(size=14, color="white"),
                        bgcolor="rgba(0,0,0,0.5)",
                        bordercolor="#4c4c4c",
                        borderwidth=1
                    )
                )
                st.plotly_chart(fig, use_container_width=True)
                
                # Metrics
                latest_price = historical['y'].iloc[-1]
                predicted_price = future_data['yhat'].iloc[-1]
                change = ((predicted_price - latest_price) / latest_price) * 100
                
                col_m1, col_m2, col_m3 = st.columns(3)
                col_m1.metric("Current Price", f"${latest_price:,.2f}")
                col_m2.metric(f"Predicted Price ({days_to_forecast} days)", f"${predicted_price:,.2f}", f"{change:.2f}%")
                col_m3.metric("Model Confidence", "80%")

    with col2:
        st.subheader("Recent Market Data")
        df_index = load_sp500_index()
        st.dataframe(
            df_index.tail(15).sort_values('Date', ascending=False).style.format({"S&P500": "${:,.2f}"}), 
            use_container_width=True,
            height=500
        )

with tabs[1]:
    st.header("Modern Portfolio Theory (MPT) Optimizer")
    
    with st.expander("ℹ️ About Portfolio Optimization", expanded=True):
        st.markdown("""
        **Objective:** Maximize returns for a given level of risk (Sharpe Ratio).
        
        **The Math:**
        We calculate the **Efficient Frontier**, the set of optimal portfolios that offer the highest expected return for a defined level of risk.
        
        $$
        Sharpe Ratio = \\frac{R_p - R_f}{\\sigma_p}
        $$
        
        Where $R_p$ is portfolio return, $R_f$ is risk-free rate, and $\\sigma_p$ is portfolio volatility.
        """)
    
    st.markdown("### Asset Selection")
    
    # Get list of tickers
    df_companies = load_sp500_companies()
    all_tickers = df_companies['Symbol'].tolist()
    
    selected_tickers = st.multiselect(
        "Select Stocks for Portfolio Construction", 
        all_tickers, 
        default=['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'TSLA', 'JPM', 'V']
    )
    
    if st.button("Run Optimization Engine"):
        if len(selected_tickers) < 2:
            st.error("Please select at least 2 stocks to build a portfolio.")
        else:
            with st.spinner("Calculating Efficient Frontier..."):
                weights, performance = optimize_portfolio(selected_tickers)
                
                if weights:
                    col_opt1, col_opt2 = st.columns([1, 1])
                    
                    with col_opt1:
                        st.subheader("Optimal Asset Allocation")
                        # Pie chart
                        labels = list(weights.keys())
                        values = list(weights.values())
                        fig_pie = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.4)])
                        fig_pie.update_layout(
                            template="plotly_dark",
                            plot_bgcolor='rgba(0,0,0,0)',
                            paper_bgcolor='rgba(0,0,0,0)',
                            legend=dict(
                                font=dict(size=14, color="white"),
                                orientation="h",
                                yanchor="bottom",
                                y=1.02,
                                xanchor="right",
                                x=1
                            )
                        )
                        st.plotly_chart(fig_pie, use_container_width=True)
                    
                    with col_opt2:
                        st.subheader("Projected Performance")
                        st.markdown("""
                        <div style='background-color: #262730; padding: 20px; border-radius: 10px;'>
                        """, unsafe_allow_html=True)
                        
                        st.metric("Expected Annual Return", f"{performance[0]*100:.2f}%", help="The estimated percentage return over the next year.")
                        st.metric("Annual Volatility (Risk)", f"{performance[1]*100:.2f}%", help="Standard deviation of returns. Lower is generally better for risk-averse investors.")
                        st.metric("Sharpe Ratio", f"{performance[2]:.2f}", help="Risk-adjusted return. >1 is good, >2 is very good, >3 is excellent.")
                        
                        st.markdown("</div>", unsafe_allow_html=True)
                        
                        st.subheader("Precise Weights")
                        st.json(weights)
                else:
                    st.error("Could not optimize. Please check data availability for selected tickers.")

with tabs[2]:
    st.header("Deep Dive: Stock Analysis")
    ticker = st.selectbox("Select Company", all_tickers)
    
    company_info = df_companies[df_companies['Symbol'] == ticker].iloc[0]
    
    col_info1, col_info2 = st.columns([1, 3])
    
    with col_info1:
        st.markdown(f"### {company_info['Shortname']}")
        st.markdown(f"**Symbol:** {ticker}")
        st.markdown(f"**Sector:** {company_info['Sector']}")
        st.markdown(f"**Industry:** {company_info['Industry']}")
        st.markdown(f"**Market Cap:** ${company_info['Marketcap']:,.0f}")
    
    with col_info2:
        # Simple chart using yfinance directly for speed in this tab
        import yfinance as yf
        if st.button("Load Real-time Price History"):
            with st.spinner(f"Fetching data for {ticker}..."):
                df_stock = yf.download(ticker, period="2y")
                if not df_stock.empty:
                    st.line_chart(df_stock['Close'], color="#00CC96")
                else:
                    st.warning("No data available.")
