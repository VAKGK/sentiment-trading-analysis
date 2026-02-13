# Crypto Trader Behavior & Market Sentiment Analysis

### 📊 Project Overview
This project analyzes the relationship between **Bitcoin Market Sentiment (Fear & Greed Index)** and **Trader Behavior (Hyperliquid Historical Data)**. The objective is to quantify how market emotion influences trading performance, risk appetite, and directional bias to uncover actionable trading strategies.

---

## 📝 Executive Summary

### 1. Methodology
To analyze the impact of sentiment on trader behavior, we performed the following data engineering and segmentation steps:

* **Data Integration:** Merged high-frequency trade data (211k rows) with daily Fear & Greed Index values by normalizing timestamps to a daily frequency.
* **Metric Definitions:**
    * **Win Rate:** Percentage of closed trades with `PnL > 0`.
    * **Risk Proxy:** Due to missing "Leverage" data, **Trade Size (USD)** was used as a proxy for risk appetite.
    * **Market Bias:** Calculated using the Long/Short ratio of opening trades.
* **User Segmentation:**
    * **Whales vs. Retail:** Traders were segmented by volume using the median Trade Size ($3,500) as the threshold.
    * **Frequent vs. Swing:** segmented by trade count frequency.

### 2. Key Insights
Our analysis revealed three statistically significant patterns:

1.  **Extreme Sentiment Drives Alpha (U-Shaped Profitability):**
    * Profitability is non-linear. Traders perform best during **Extreme Greed** (Avg PnL: $130) and **Fear** (Avg PnL: $112).
    * **Neutral** markets yield the lowest returns ($71), likely due to a lack of clear trend direction (chop).

2.  **The "Smart Money" Accumulates in Fear:**
    * Contrary to the expectation of panic selling, the **Average Trade Size** is highest during **Fear ($7,816)**.
    * This indicates that high-conviction traders ("Whales") use fear as a liquidity event to accumulate large positions.

3.  **Crowd Behavior is Contrarian:**
    * Traders correctly anticipate reversals. The **Long/Short Ratio** flips from **2.21 (Long)** in Extreme Fear to **0.73 (Short)** in Greed.
    * The crowd successfully "buys the dip" and "sells the strength."

### 3. Strategy Recommendations
Based on the data, we propose the following algorithmic rules:

* **Strategy A: The "Fear Accumulation" Protocol**
    * **Trigger:** Sentiment Index drops to "Fear" (< 40).
    * **Action:** Increase average position size by **30%** and strictly **avoid Shorting**.
    * **Rationale:** "Fear" days offer a unique combination of high Win Rate (87%) and high average returns ($112). It is statistically the safest time to deploy large capital.

* **Strategy B: The "Greed Momentum" Hold**
    * **Trigger:** Sentiment shifts to "Greed" (> 60).
    * **Action:** Switch from High-Frequency Scalping to **Swing Trading** (Hold > 24h).
    * **Rationale:** While the crowd starts shorting early in "Greed" (Ratio 0.73), the highest profits ($130/trade) occur in the subsequent "Extreme Greed" phase. Holding Longs captures the "irrational exuberance" premium.

---

## 🛠️ Technical Setup

### Prerequisites
* Python 3.8+
* Libraries: `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `streamlit`, `plotly`

### Project Structure
```bash
├── data/
│   ├── fear_greed_index.csv
│   └── historical_data.csv
├── notebooks/
│   └── Trader_Performance_Analysis.ipynb        # Core analysis and visualizations
├── app.py                                       # Streamlit Dashboard
├── README.md                                    # Project Documentation
└── requirements.txt                             # Dependencies
