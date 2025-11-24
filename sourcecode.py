import tkinter as tk
from tkinter import ttk, messagebox
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Define the stock symbols you want to track (use correct tickers)
STOCKS = ['AAPL', 'GOOGL', 'MSTR', 'TSLA', 'AMZN', '^GSPC']

def get_stock_data(symbol):
    try:
        df = yf.Ticker(symbol).history(period='100d')
        return df
    except Exception as e:
        messagebox.showerror("Error", f"Data fetch failed: {str(e)}")
        return None

def plot_stock(df, symbol, ax):
    ax.clear()
    if df is not None and not df.empty:
        ax.plot(df.index, df['Close'], label='Close', color='cyan')
        ax.plot(df.index, df['Close'].rolling(window=20).mean(), label='MA20', color='orange')
        ax.set_title(symbol, color='white')
        ax.grid(True, color='gray')
        ax.legend(facecolor='black', edgecolor='gray', labelcolor='white')
        ax.tick_params(colors='white')
        ax.set_facecolor('black')
        fig = ax.get_figure()
        fig.patch.set_facecolor('black')
    else:
        ax.text(0.5, 0.5, "No Data Found", ha='center', color='red', transform=ax.transAxes)

def predict_next(df):
    if df is None or df.empty:
        return None
    X = np.arange(len(df)).reshape(-1, 1)
    y = df['Close'].values
    model = LinearRegression()
    try:
        model.fit(X, y)
        next_val = model.predict(np.array([[len(df)]]))[0]
        return next_val
    except Exception as e:
        return None

def show_stock(symbol):
    df = get_stock_data(symbol)
    plot_stock(df, symbol, ax)
    canvas.draw()
    prediction = predict_next(df)
    if prediction:
        lbl_pred.config(text=f"Prediction for next day: {prediction:.2f}", fg='lime')
    else:
        lbl_pred.config(text="No prediction available.", fg='red')

def show_best_stock():
    scores = []
    for sym in STOCKS:
        df = get_stock_data(sym)
        if df is not None and not df.empty:
            ret = df['Close'].pct_change().mean()
            scores.append((sym, ret))
    scores.sort(key=lambda x: x[1], reverse=True)
    text_suggest.config(state=tk.NORMAL)
    text_suggest.delete('1.0', tk.END)
    for s, score in scores[:3]:
        text_suggest.insert(tk.END, f"Top pick: {s} (Avg. Return: {score:.4f})\n")
    text_suggest.config(state=tk.DISABLED)

# Main GUI
root = tk.Tk()
root.title("Stock Dashboard")
root.geometry("950x600")
root.config(bg="black")

frame_sidebar = tk.Frame(root, bg="black")
frame_sidebar.pack(side=tk.LEFT, fill=tk.Y)
tk.Label(frame_sidebar, text="Stocks", font=("Arial", 16), bg="black", fg="cyan").pack(pady=10)
for sym in STOCKS:
    tk.Button(frame_sidebar, text=sym, font=("Arial", 12),
              bg="#222222", fg="lime", activebackground="#333333",
              activeforeground="cyan", command=lambda sym=sym: show_stock(sym)).pack(fill=tk.X, pady=3)

frame_main = tk.Frame(root, bg="black")
frame_main.pack(expand=True, fill=tk.BOTH)

notebook = ttk.Notebook(frame_main)
notebook.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

tab_market = tk.Frame(notebook, bg="black")
notebook.add(tab_market, text="Market")

fig, ax = plt.subplots(figsize=(7, 4))
canvas = FigureCanvasTkAgg(fig, master=tab_market)
canvas.get_tk_widget().pack(expand=True, fill=tk.BOTH)

lbl_pred = tk.Label(tab_market, text="", font=("Arial", 13), bg="black", fg="lime")
lbl_pred.pack(pady=8)

tab_suggest = tk.Frame(notebook, bg="black")
notebook.add(tab_suggest, text="Suggestion")
tk.Button(tab_suggest, text="Show Best Stocks",
          font=("Arial", 12), bg="#222222", fg="cyan", 
          activebackground="#444444", activeforeground="lime", command=show_best_stock).pack(pady=10)
text_suggest = tk.Text(tab_suggest, font=("Arial", 12),
                 bg="#101010", fg="white", width=50, height=7, state=tk.DISABLED)
text_suggest.pack(pady=10)

root.mainloop()
