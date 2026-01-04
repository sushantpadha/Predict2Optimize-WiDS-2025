import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Helpers: save / load predicted returns and covariance
# ============================================================

def save_predictions(mu_hat, Sigma_hat, tickers, path="predictions.npz"):
    """
    Save predicted mean returns and covariance to disk.
    """
    np.savez(
        path,
        mu_hat=np.asarray(mu_hat),
        Sigma_hat=np.asarray(Sigma_hat),
        tickers=np.asarray(tickers)
    )


def load_predictions(path="predictions.npz"):
    """
    Load predicted mean returns and covariance from disk.
    """
    data = np.load(path, allow_pickle=True)
    mu_hat = data["mu_hat"]
    Sigma_hat = data["Sigma_hat"]
    tickers = data["tickers"].tolist()

    return mu_hat, Sigma_hat, tickers


# ============================================================
# Helper: visualization of inputs
# ============================================================

def plot_mu_and_cov(mu, Sigma, tickers=None):
    """
    Visualize mean returns and covariance matrix as heatmaps.
    """
    n = len(mu)
    labels = tickers if tickers is not None else [f"A{i}" for i in range(n)]

    # Mean returns
    plt.figure(figsize=(6, 1.5))
    plt.imshow(mu.reshape(1, -1), aspect="auto", cmap="coolwarm")
    plt.colorbar(label="Expected return")
    plt.yticks([])
    plt.xticks(range(n), labels)
    plt.title("Predicted mean returns")
    plt.show()

    # Covariance matrix
    plt.figure(figsize=(6, 5))
    plt.imshow(Sigma, cmap="viridis")
    plt.colorbar(label="Covariance")
    plt.xticks(range(n), labels, rotation=45)
    plt.yticks(range(n), labels)
    plt.title("Predicted covariance matrix")
    plt.tight_layout()
    plt.show()

# =============================================
# Helper: Visualize portfolio as stacked weights
# =============================================

def visualize_weights_stacked(weights, labels=None, tickers=None):
    """
    weights: array of shape (n_lambda, n_assets)
    """
    weights = np.asarray(weights)
    n_lambda, n_assets = weights.shape

    plt.figure(figsize=(12, 5))
    bottom = np.zeros(n_lambda)

    for j in range(n_assets):
        plt.bar(
            range(n_lambda),
            weights[:, j],
            bottom=bottom,
            width=0.8,
            label=(tickers[j] if tickers else f"Asset {j+1}")
        )
        bottom += weights[:, j]

    plt.xlabel(r"Risk aversion parameter $\lambda$")
    plt.ylabel("Portfolio weight")
    plt.title("Portfolio composition vs risk aversion")

    plt.xticks(
        ticks=range(n_lambda),
        labels=(labels if labels else range(n_lambda)),
        rotation=45
    )

    plt.ylim(0, 1.0)
    plt.legend()
    plt.tight_layout()
    plt.show()


# ==========================================
# Helper: Visualize portfolio in (Return, Risk) space
# ==========================================

def visualize_return_risk(returns, variances, labels, use_volatility=True):
    """
    returns: expected returns
    variances: portfolio variances
    """
    x = np.sqrt(variances) if use_volatility else variances
    xlabel = "Volatility" if use_volatility else "Variance"

    plt.figure(figsize=(6, 5))
    plt.plot(x, returns, marker="o")

    for lb, xi, r in zip(labels, x, returns):
        plt.annotate(
            lb,
            (xi, r),
            textcoords="offset points",
            xytext=(5, 5),
            fontsize=8
        )

    plt.xlabel(xlabel)
    plt.ylabel("Expected return")
    plt.title("Efficient Frontier (Markowitz)")
    plt.grid(True)
    plt.show()


# ============================================================
# Helper: Sharpe Ratio
# ============================================================
def compute_sharpe_ratios(weights, mu, Sigma, eps=1e-8):
    """
    weights: array of shape (n_lambda, n_assets)
    mu: mean returns (n_assets,)
    Sigma: covariance matrix (n_assets, n_assets)

    Returns:
        sharpe: array of shape (n_lambda,)
        returns: array of expected returns
        variances: array of variances
    """
    weights = np.asarray(weights)
    mu = np.asarray(mu)
    Sigma = np.asarray(Sigma)

    returns = weights @ mu
    variances = np.einsum("ij,jk,ik->i", weights, Sigma, weights)

    sharpe = returns / (np.sqrt(variances) + eps)
    return sharpe, returns, variances


def plot_sharpe_ratios(sharpe, labels=None):
    """
    sharpe: array of Sharpe ratios
    """
    sharpe = np.asarray(sharpe)

    plt.figure(figsize=(6, 4))
    plt.plot(range(len(sharpe)), sharpe, marker="o")
    plt.xlabel(r"Risk aversion parameter $\lambda$")
    plt.ylabel("Sharpe ratio")
    plt.title("Sharpe ratio vs risk aversion")
    plt.grid(True)

    if labels is not None:
        plt.xticks(range(len(sharpe)), labels, rotation=45)

    plt.tight_layout()
    plt.show()


def print_sharpe_table(labels, sharpe, returns, variances):
    print(f"{'λ':>10} | {'Return':>10} | {'Volatility':>12} | {'Sharpe':>10}")
    print("-" * 52)
    for lb, r, v, s in zip(labels, returns, variances, sharpe):
        print(f"{lb:>10} | {r:10.4f} | {np.sqrt(v):12.4f} | {s:10.4f}")
