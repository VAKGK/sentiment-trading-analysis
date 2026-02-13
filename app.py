import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("Crypto Trader Behavior & Sentiment Dashboard")


# --- 1. Load & Merge Data (The Fix) ---
@st.cache_data
def load_data():
    # A. Load both original CSV files
    # Make sure these files are in the same folder as this script
    sentiment_df = pd.read_csv('fear_greed_index.csv')
    trades_df = pd.read_csv('historical_data.csv')

    # B. Fix Dates (Same logic as your analysis)
    sentiment_df['Date'] = pd.to_datetime(sentiment_df['date'])

    # Handle the specific timestamp format in your trade data
    trades_df['time'] = pd.to_datetime(trades_df['Timestamp IST'], dayfirst=True)
    trades_df['Date'] = trades_df['time'].dt.normalize()

    # C. Merge them
    merged_df = pd.merge(trades_df, sentiment_df[['Date', 'value', 'classification']], on='Date', how='left')

    # D. Clean up (Optional: Drop rows with missing sentiment)
    merged_df = merged_df.dropna(subset=['classification'])

    return merged_df


# --- 2. Dashboard Logic ---
try:
    df = load_data()

    # Sidebar Filter
    st.sidebar.header("Filters")
    sentiment = st.sidebar.selectbox("Select Market Sentiment", df['classification'].unique())

    # Filter Data based on selection
    filtered_df = df[df['classification'] == sentiment]

    # --- KPI Section ---
    st.write(f"### Performance during '{sentiment}'")

    avg_pnl = filtered_df['Closed PnL'].mean()
    win_rate = (filtered_df['Closed PnL'] > 0).mean() * 100
    total_trades = len(filtered_df)

    col1, col2, col3 = st.columns(3)
    col1.metric("Avg PnL", f"${avg_pnl:.2f}")
    col2.metric("Win Rate", f"{win_rate:.1f}%")
    col3.metric("Total Trades", f"{total_trades:,}")

    # --- Charts Section ---

    # Chart 1: PnL Distribution
    st.subheader("1. PnL Distribution")
    fig_hist = px.histogram(
        filtered_df,
        x="Closed PnL",
        nbins=50,
        title=f"Distribution of Trade Results in {sentiment}",
        color_discrete_sequence=['#636EFA']
    )
    st.plotly_chart(fig_hist)

    # Chart 2: Risk (Size) vs Reward (PnL)
    st.subheader("2. Risk vs. Reward Analysis")
    st.markdown("Does taking larger positions (higher risk) lead to higher profits?")
    fig_scatter = px.scatter(
        filtered_df,
        x="Size USD",
        y="Closed PnL",
        color="Side",
        title="Trade Size vs. PnL",
        opacity=0.6
    )
    st.plotly_chart(fig_scatter)

except Exception as e:
    st.error(f"Error loading data: {e}")
    st.write("Please ensure 'fear_greed_index.csv' and 'historical_data.csv' are in the same folder.")