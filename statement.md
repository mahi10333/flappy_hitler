# Project Statement: Simple Stock Market Dashboard

## Problem Statement

In the fast-paced world of financial markets, individual investors and students often lack a simple, consolidated, and free tool to quickly analyze short-term stock performance and trends. Existing solutions are often overloaded with complex features, require paid subscriptions, or are difficult to integrate for basic analysis and learning.

**The core problem is the need for an accessible, open-source desktop application that provides immediate graphical visualization of stock prices and a simple, quantitative outlook (prediction) without requiring an external web browser or complex setup.**

## Scope of the Project

The project is scoped to deliver a functional, minimal-feature **desktop application** focused on short-term technical analysis and basic forecasting.

### In Scope
* **Data Access:** Fetching daily historical data for a small, predefined list of major US stock tickers.
* **Visualization:** Displaying fundamental price data (Close) and one key technical indicator (20-day Moving Average) using an integrated chart.
* **Basic Forecasting:** Implementing a simple linear regression model to demonstrate the concept of next-day price prediction.
* **User Experience:** Providing a dark-themed, click-and-view GUI for easy interaction.

### Out of Scope (Future Enhancements)
* **Real-time Streaming Data:** Data updates will be static upon button click, not streamed in real-time.
* **Complex Models:** Advanced predictive models (e.g., ARIMA, LSTMs) are excluded.
* **Portfolio Management:** The application will not track user investments, trades, or portfolio value.
* **Custom Ticker Input:** Users cannot dynamically add new stock tickers during runtime.



## Target Users

The Stock Dashboard is primarily aimed at two groups:

1.  **Beginner Investors & Students:** Individuals new to stock market analysis who need a simple tool to visualize basic trends (price, MA) and understand the concept of quantitative analysis.
2.  **Developers & Learners of Python GUI:** Users interested in seeing a practical example of integrating disparate Python libraries (**Tkinter**, **Matplotlib**, **yfinance**, **Scikit-learn**) into a cohesive desktop application.



## High-Level Features

| Feature Category | Description |

| **Data Retrieval** | Ability to fetch and process **100 days** of historical data for a predefined set of key stock tickers using `yfinance`. |
| **Technical Analysis** | Display of the stock's **Closing Price** along with the **20-day Simple Moving Average (MA20)** overlaid on a single chart. |
| **Predictive Modeling** | A basic **Linear Regression** feature to project the likely closing price for the **next trading day**. |
| **Performance Ranking** | A **Suggestion** tab that calculates and displays the stocks with the highest **average daily percentage return** over the lookback period. |
| **User Interface** | An intuitive, dark-themed **Tkinter GUI** with clearly labeled buttons for navigation and data access. |
