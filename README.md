# 📊 Sentiment & Trader Behavior Analysis

### **Quantifying the Impact of Fear & Greed on Trading Performance**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)]()

---

## 📖 Overview

**Do markets move on logic or emotion?**

This project analyzes the relationship between **Bitcoin Market Sentiment** (measured by the Fear & Greed Index) and **Trader Behavior** (using Hyperliquid historical trade data). The objective was to quantify how emotional states influence trading performance, risk appetite, and directional bias.

By merging high-frequency trade data with daily sentiment values, we uncovered actionable patterns that can be used to optimize trading strategies.

> *"Alpha exists at the extremes of human emotion."*

---

## 🔍 Key Insights & Findings

Our analysis of over **211k trades** revealed three statistically significant patterns:

* **🚀 Extreme Sentiment Drives Alpha:** Profitability follows a U-shaped curve. Traders perform best during **Extreme Greed** (Avg PnL: $130) and **Fear** (Avg PnL: $112), while **Neutral** markets yield the lowest returns due to lack of direction.
* **🐋 Smart Money Accumulates in Fear:** Contrary to panic selling, the **Average Trade Size** is highest during Fear ($7,816), indicating that high-conviction traders ("Whales") use fear events to accumulate large positions.
* **🧠 Crowd Behavior is Contrarian:** Traders correctly anticipate reversals. The **Long/Short Ratio** flips from **2.21 (Long)** in Extreme Fear to **0.73 (Short)** in Greed, showing the crowd successfully "buys the dip" and "sells the strength."

---

## 💡 Strategy Recommendations

Based on the data, we propose two algorithmic rules for improved performance:

### **Strategy A: The "Fear Accumulation" Protocol**
* **🚨 Trigger:** Sentiment Index drops to "Fear" (< 40).
* **⚡ Action:** Increase average position size by **30%** and strictly **avoid Shorting**.
* **Rationale:** "Fear" days offer a unique combination of high Win Rate (87%) and high average returns. It is statistically the safest time to deploy large capital.

### **Strategy B: The "Greed Momentum" Hold**
* **🚨 Trigger:** Sentiment shifts to "Greed" (> 60).
* **⚡ Action:** Switch from High-Frequency Scalping to **Swing Trading** (Hold > 24h).
* **Rationale:** While the crowd starts shorting early in "Greed" (Ratio 0.73), the highest profits ($130/trade) occur in the subsequent "Extreme Greed" phase. Holding Longs captures the "irrational exuberance" premium.

---

## 🛠️ Technical Implementation

### **Prerequisites**
* Python 3.8+
* Libraries: `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `streamlit`, `plotly`

### **Methodology**
1. **Data Integration:** Merged high-frequency trade data with daily Fear & Greed Index values.
2. **Metric Definitions:**
    * **Win Rate:** Percentage of closed trades with PnL > 0.
    * **Risk Proxy:** Used Trade Size (USD) as a proxy for risk appetite.
    * **Market Bias:** Calculated using the Long/Short ratio of opening trades.
3. **User Segmentation:**
    * **Whales vs. Retail:** Segmented by trade volume (Median: $3,500).
    * **Frequent vs. Swing:** Segmented by trade count frequency.

---

## ⚙️ The Workflow

```mermaid
graph TD;
    A["📂 Historical Trade Data
    (Hyperliquid)"] -->|Merge & Clean| C{"⚙️ Data Integration (Pandas)"};
    B["😨 Fear & Greed Index
    (Daily CSV)"] -->|Normalize Timestamp| C;
    C -->|Segmentation| D["👥 User Profiling
        (Whales vs. Retail)"];
    D -->|Analysis| E["📊 Performance Metrics (Win Rate, PnL, Bias)"];
    E -->|Strategy| F["💡 Actionable Insights (Fear Accumulation Rule)"];

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#f9f,stroke:#333,stroke-width:2px
    style E fill:#bbf,stroke:#333,stroke-width:2px
    style F fill:#bfb,stroke:#333,stroke-width:2px
