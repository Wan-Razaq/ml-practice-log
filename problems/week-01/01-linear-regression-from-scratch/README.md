# Linear Regression from Scratch

**Difficulty:** Easy
**Week:** 1
**Date:** 2026-09-23
**Dataset/Source:** California Housing (sklearn's built-in `fetch_california_housing`)

## Problem

Predict median house value for a district from features like median income, average rooms, and location. Goal: implement ordinary least squares linear regression using only NumPy (no `sklearn.linear_model`), and get within a reasonable margin of sklearn's own implementation on the same split, measured by RMSE.

## Approach

- Implemented gradient descent manually: initialize weights at zero, compute predictions, compute MSE loss, compute gradients, update weights in a loop.
- Standardized features first (zero mean, unit variance) — without this, gradient descent diverged with a learning rate that worked fine after scaling.
- Compared my from-scratch model's final RMSE against `sklearn.linear_model.LinearRegression` trained on the same split, as a correctness check.

## Code

See [`solution.py`](solution.py).

## Results

- My implementation RMSE: `<fill in after running>`
- sklearn RMSE: `<fill in after running>`
- Difference: `<fill in>` — small enough to confirm the manual implementation converged correctly.

## Learnings

- Feature scaling isn't optional for gradient descent — it changes whether the same learning rate converges or diverges.
- Watching the loss curve per iteration is the fastest way to catch a bad learning rate before wasting time debugging the math.
- Next time: try implementing the closed-form normal equation solution too, and compare speed vs. gradient descent on the same dataset.
