import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

sns.set_theme(style="darkgrid")

# ============================================================
# Get returns data
# ============================================================

def load_return_data(tickers, start, end, freq="1d", dropna=True,):
    """
    Download price data and compute simple (linear) returns.

    tickers : list of str
    start, end : str (YYYY-MM-DD).
    freq : str (default: daily).
    dropna : bool (default: True)

    Returns: pd.DataFrame
        DataFrame of linear returns with shape (T, n_assets).
        Rows are dates, columns are tickers.
    """

    data = yf.download(tickers, start=start, end=end, interval=freq, auto_adjust=False, progress=False, )
    prices = pd.DataFrame(data["Adj Close"][tickers])
    prices.bfill().ffill()  # fill in empty rows

    # compute linear returns: r_t = (P_t / P_{t-1}) - 1
    returns = prices.pct_change()

    # drop the first row
    returns = returns.iloc[1:]

    if dropna:
        returns = returns.dropna(how="any")

    return returns


# ============================================================
# Wealth and return plots
# ============================================================

def plot_wealth(wealth, dates=None, title="Portfolio Wealth"):
    plt.figure(figsize=(10, 4))
    plt.plot(wealth, linewidth=2)
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Net Wealth")
    if dates is not None:
        plt.xticks(range(0, len(dates), max(1, len(dates)//8)), dates[::max(1, len(dates)//8)], rotation=45)
    plt.tight_layout()
    plt.show()


def plot_returns(returns, title="Daily Portfolio Returns"):
    plt.figure(figsize=(10, 3))
    plt.plot(returns, alpha=0.7)
    plt.axhline(0.0, color="black", linewidth=1)
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Return")
    plt.tight_layout()
    plt.show()


# ============================================================
# Weights and turnover diagnostics
# ============================================================

def plot_weights_over_time(weights, tickers):
    """
    Plot individual asset weights over time.

    weights : array of shape (T, n_assets)
    """
    plt.figure(figsize=(12, 4))
    for i, tkr in enumerate(tickers):
        plt.plot(weights[:, i], label=tkr)
    plt.title("Portfolio weights over time")
    plt.xlabel("Time")
    plt.ylabel("Weight")
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    
def plot_weights_stacked_area(weights, tickers, dates=None, freq="weekly"):
    """
    Plot portfolio composition as a stacked area chart.

    weights : array of shape (T, n_assets)
    tickers : list of asset names
    dates : list-like of dates (optional)
    freq : {"daily", "weekly"} or int
        Controls x-axis label spacing.
    """
    weights = np.asarray(weights)
    T = weights.shape[0]
    x = np.arange(T)

    plt.figure(figsize=(12, 4))
    plt.stackplot(
        x,
        weights.T,
        labels=tickers,
        alpha=0.9,
    )

    plt.title("Portfolio composition over time")
    plt.xlabel("Time")
    plt.ylabel("Weight")

    if dates is not None:
        if freq == "daily":
            step = max(1, T // 10)
        elif freq == "weekly":
            step = 5
        elif isinstance(freq, int):
            step = freq
        else:
            step = max(1, T // 10)

        ticks = np.arange(0, T, step)
        tick_labels = [dates[i] for i in ticks]
        plt.xticks(ticks, tick_labels, rotation=45)

    plt.legend(loc="upper left", ncol=2)
    plt.tight_layout()
    plt.show()


def plot_turnover(turnover):
    plt.figure(figsize=(10, 3))
    plt.plot(turnover, linewidth=2)
    plt.title("Portfolio Turnover")
    plt.xlabel("Time")
    plt.ylabel("Turnover")
    plt.tight_layout()
    plt.show()


# ============================================================
# Simple performance summary
# ============================================================

def print_performance_summary(wealth, returns):
    total_return = wealth[-1] / wealth[0] - 1.0
    avg_return = np.mean(returns)
    vol = np.std(returns)

    print("Performance summary")
    print("-------------------")
    print(f"Total return:     {total_return:.2%}")
    print(f"Avg daily return: {avg_return:.4f}")
    print(f"Daily volatility: {vol:.4f}")
