(This repository contains my midterm work for the Predict2Optimize program, covering Week 1 and Week 2.
The focus of this work was to understand financial time-series data, compute returns and volatility, and 
build baseline prediction models for stock returns using proper time-series evaluation.
The goal was to develop evaluation discipline, understand the difficulty of financial prediction, and avoid 
common pitfalls such as look-ahead bias.)

Week 1: Basic Financial Data Analysis
        •	Source: Yahoo Finance (yfinance)

        •	Assets: AAPL, MSFT, GOOG, AMZN, TSLA

        •	Time Horizons:
            1. Long-term: 2015–2024
            2. Medium-term: 2020–2024 (includes COVID period)


    Key Concepts Used
        •	Adjusted Close price: Used instead of raw close prices for stock splits and dividends.

        •	Returns:
            Simple returns and log returns
            Log returns were preferred for analysis due to better statistical properties.

        •	Volatility:
            Rolling standard deviation over multiple windows
            Observed volatility clustering, especially during market stress.

        •	Rolling mean and variance analysis
    

    Observations
        •	Prices are non-stationary, but log returns are approximately stationary.
        •	High-volatility periods (e.g., March 2020) lead to large market drawdowns.
        •	Volatility tends to cluster rather than remain constant over time.


Week 2: Baseline Models & Time-Series Evaluation

        Financial return prediction is extremely noisy.Before using complex models, it is essential 
        to establish strong naive baselines to understand whether a model is actually learning signal or just noise.

    Models Used : 
        1.	Zero-return predictor
        	Always predicts a return of zero.
        	Strong sanity check since daily returns have mean close to zero.

        2.	Rolling mean predictor
        	Predicts the next-day return using the rolling average of recent returns.
        	Introduction to  time dependence (without use of ML).

        3.	OLS (Linear Regression)
            •	Features used like : Today’s return	,Yesterday’s return	, 20-day rolling mean , 20-day rolling volatility , 5-day momentum
            •	Trained and evaluated using walk-forward validation.

    Evaluation Methods
        •	TimeSeriesSplit (walk-forward) was used instead of random train-test splits.
        •	Metrics used like MSE and RMSE to avoid look-ahead bias and more likely to match real-world changes.

    Results Summary
    Zero Predictor ~ 0.0186
    Rolling Mean.  ~ 0.0190
    OLS ~ 0.0187

Interpretation
	1.  The zero-return predictor performed competitively, highlighting how difficult it is to beat simple baselines in finance.
	2.  OLS model did not significantly outperform the naive baseline, in this case .
	3.	This shows the idea that financial markets have low signal-to-noise ratios.
    4.  Complex models do not guarantee better performance.