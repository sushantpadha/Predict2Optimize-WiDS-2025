# Further Exploration

This section is meant as a **gentle set of directions**, not a checklist. Thanks for putting in the time and effort — I hope you enjoyed building, breaking, and questioning your own portfolio strategies.

---

## Convex optimization (the backbone)

> “The great watershed in optimization isn’t between smooth and nonsmooth problems, but between convex and nonconvex problems.”
> ~R. Tyrrell Rockafellar

Much of what you’ve done rests on ideas from **convex optimization**, even if we kept the machinery mostly in the background.

If you want a clearer picture of *why* mean–variance optimization works, *why* robustness introduces regularization, and *why* some formulations are numerically stable while others are not, learning a bit more convex optimization is extremely worthwhile.

A very practical and approachable starting point is **Stephen Boyd’s material**:
- *Convex Optimization* (Boyd & Vandenberghe)
- The Stanford course taught alongside it
- The lecture slides are particularly good:  
  https://stanford.edu/~boyd/cvxbook/bv_cvxslides.pdf  
  (Chapter 4 is an excellent introduction to how convex problems are structured.)

Boyd’s treatment is geometric and algorithmic, which fits portfolio optimization very naturally.

For a more **theoretical and rigorous** perspective, a complementary reference is:
- *Convex Optimization Theory* - Dimitri Bertsekas

Bertsekas focuses more on duality, sensitivity, and perturbation analysis — ideas that explain why optimized portfolios can be fragile and how regularization helps. It also provides a more elegant framework for explaining it, as opposed to the usual motivation for lagrange multipliers.

A modern treatment of the classic markowitz formulation with the standard practical constraints can be found in this [paper](https://web.stanford.edu/~boyd/papers/pdf/markowitz.pdf).

---

## Potential optimization tasks and more complex portfolios

Once you’re comfortable with basic mean–variance optimization, there are many natural extensions that stay within the same conceptual framework:

- **Second-order portfolio formulations**  
  Reformulate variance or risk constraints as second-order cone programs (SOCPs) and explore alternative risk measures such as CVaR.

- **Sharpe ratio maximization**  
  Direct Sharpe maximization is nonconvex, but it can be handled via **iterative convex or SCP-style schemes** (e.g. fractional programming, fixing risk and maximizing return in a loop).

- **Transaction-aware optimization**  
  Penalizing $\|w - w_{\text{prev}}\|$ directly in the objective leads to smoother, more realistic portfolios and highlights the interaction between optimization and execution.

- **Robust optimization**  
  Modeling uncertainty in expected returns or covariance explicitly leads to structured regularization and more stable allocations.

A natural way to move beyond is to look at standard implementations, such as the [PyPortfolioOpt](https://pyportfolioopt.readthedocs.io/en/latest/) library, which (I hope) you'll have a newfound appreciation for.

---

## Financial modeling and estimation

If you found the modeling side more interesting, there is plenty of depth to explore there as well:

- **Improved covariance estimation**  
  EWMA, shrinkage estimators (e.g. Ledoit–Wolf), and low-rank approximations can dramatically improve stability.

- **Factor models**  
  Modeling returns via factors (economic or statistical) reduces dimensionality and often produces more robust portfolios.

- **Better return modeling**  
  Simple time-series structure, regularized predictors, or factor-based forecasts can outperform naive rolling means.

- **Analysis techniques**  
  Rolling performance metrics, sensitivity analysis, turnover diagnostics, and stress testing all help you understand *why* a strategy behaves as it does.

A particularly nice reference which focusses on a factor-based asset model is:
- [Hudson River Trading - *Modeling Equity Returns*](https://www.hudsonrivertrading.com/hrtbeat/modeling-equities-returns/)

---

## Closing thought

This project wasn’t about finding the “best” portfolio. It was about learning how prediction, optimization, and uncertainty interact in practice.

If you walk away with a better intuition for convexity, estimation error, and the limits of optimization, then this project has done its job.

I hope this was both challenging and fun.
