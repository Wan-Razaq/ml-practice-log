"""
Linear Regression from Scratch
Week 1, Problem 1 — Easy

Implements OLS linear regression via batch gradient descent using only NumPy,
then compares RMSE against sklearn's LinearRegression as a correctness check.
"""

import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error


def train_linear_regression(X, y, lr=0.1, n_iters=1000):
    """Batch gradient descent for OLS linear regression."""
    n_samples, n_features = X.shape
    weights = np.zeros(n_features)
    bias = 0.0

    for _ in range(n_iters):
        y_pred = X @ weights + bias
        error = y_pred - y

        dw = (2 / n_samples) * (X.T @ error)
        db = (2 / n_samples) * np.sum(error)

        weights -= lr * dw
        bias -= lr * db

    return weights, bias


def predict(X, weights, bias):
    return X @ weights + bias


def main():
    data = fetch_california_housing()
    X, y = data.data, data.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # --- My implementation ---
    weights, bias = train_linear_regression(X_train_scaled, y_train, lr=0.1, n_iters=1000)
    y_pred_mine = predict(X_test_scaled, weights, bias)
    rmse_mine = np.sqrt(mean_squared_error(y_test, y_pred_mine))

    # --- sklearn, for comparison ---
    sk_model = LinearRegression()
    sk_model.fit(X_train_scaled, y_train)
    y_pred_sklearn = sk_model.predict(X_test_scaled)
    rmse_sklearn = np.sqrt(mean_squared_error(y_test, y_pred_sklearn))

    print(f"My implementation RMSE: {rmse_mine:.4f}")
    print(f"sklearn RMSE:           {rmse_sklearn:.4f}")
    print(f"Difference:             {abs(rmse_mine - rmse_sklearn):.4f}")


if __name__ == "__main__":
    main()
