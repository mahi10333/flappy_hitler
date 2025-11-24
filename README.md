# flappy hitler
VITYARTHI Project

# Simple Stock Market Dashboard with Prediction

## Project Overview

This project is a desktop application built using Python's **Tkinter** library to create an interactive stock market dashboard. It fetches real-time historical stock data using the **`yfinance`** library, visualizes price trends with **`matplotlib`**, and provides a basic next-day closing price prediction using **Linear Regression**.

The dashboard offers a dark-themed, user-friendly interface for tracking the performance of selected stocks and receiving simple investment suggestions.

## Features

* **Real-Time Data Fetching:** Downloads the last 100 days of stock data for selected tickers (AAPL, GOOGL, TSLA, etc.) from Yahoo Finance.
* **Interactive Visualization:** Displays a **closing price chart** and a **20-day Simple Moving Average (MA20)** for easy trend analysis.
* **Simple Price Prediction:** Uses a **Linear Regression** model to predict the next trading day's closing price.
* **Top Stock Suggestion:** Calculates and ranks stocks based on their **average daily percentage return** to suggest potential top performers.
* **Dark Theme GUI:** A clean, dark-mode interface built with Tkinter and Matplotlib.

## Technologies & Tools Used

The project is built entirely in **Python** and relies on the following key libraries:

| Technology | Purpose |
| :--- | :--- |
| **Python 3.x** | Core programming language. |
| **`tkinter`** | Framework for creating the desktop **Graphical User Interface (GUI)**. |
| **`yfinance`** | A reliable and easy-to-use library for downloading **historical stock data**. |
| **`matplotlib`** | Used for creating the stock price charts and technical analysis visualization. |
| **`pandas`** & **`numpy`** | Essential for data handling, cleaning, and mathematical operations. |
| **`scikit-learn`** | Used for the **Linear Regression** model implementation for price prediction. |

---

## Steps to Install & Run the Project

### Prerequisites

You need **Python 3.x** installed on your system.

### 1. Clone the Repository

```bash
git clone <repository-url>
cd stock-dashboard
