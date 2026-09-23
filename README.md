# ML Practice Log 🚀

A structured repo for consistent machine learning practice — one problem at a time, building a public GitHub portfolio as I go.

## How this works

- **3–4 problems per week**
- Difficulty progresses **Easy → Medium → Hard** over 12 weeks (see [`ROADMAP.md`](ROADMAP.md))
- Every problem gets its own folder with a consistent write-up: **Problem → Approach → Code → Results → Learnings**
- Run `scripts/new_problem.sh` to scaffold a new problem folder from the template in one command

## Folder structure

```
ml-practice/
├── README.md                 <- you are here (overview + tracker)
├── ROADMAP.md                 <- full 12-week problem list
├── templates/
│   └── PROBLEM_TEMPLATE.md    <- the write-up format every problem follows
├── scripts/
│   └── new_problem.sh         <- scaffolds a new problem folder
└── problems/
    ├── week-01/
    │   ├── 01-linear-regression-from-scratch/
    │   │   ├── README.md
    │   │   └── solution.py
    │   ├── 02-titanic-survival-classifier/
    │   └── 03-knn-from-scratch/
    ├── week-02/
    └── ...
```

## Why this format

- **Consistency beats intensity.** 3–4 problems/week is sustainable and still fills the contribution graph steadily.
- **The README-per-problem habit** is what makes the repo readable to *other people* (recruiters, collaborators) — not just green squares.
- **Easy → Medium → Hard** mirrors how you'd actually build skill: fundamentals first, then techniques, then from-scratch/deep implementations.

## Progress tracker

Check items off as you go — GitHub renders `- [x]` checkboxes automatically.

### Week 1–4: Easy

- [ ] W1.1 — Linear Regression from Scratch
- [ ] W1.2 — Titanic Survival Classifier
- [ ] W1.3 — K-Nearest Neighbors from Scratch
- [ ] W2.1 — Decision Tree Classifier
- [ ] W2.2 — Data Cleaning & EDA Challenge
- [ ] W2.3 — Naive Bayes Spam Classifier
- [ ] W2.4 — K-Means Clustering from Scratch
- [ ] W3.1 — Cross-Validation & Metrics Deep Dive
- [ ] W3.2 — Feature Engineering Practice
- [ ] W3.3 — Simple Movie Recommender
- [ ] W4.1 — Gradient Descent from Scratch
- [ ] W4.2 — Handling Imbalanced Data
- [ ] W4.3 — Time Series Plotting & Moving Average Forecast
- [ ] W4.4 — Confusion Matrix & ROC Curve Visualizer

### Week 5–8: Medium

- [ ] W5.1 — Random Forest vs Gradient Boosting Comparison
- [ ] W5.2 — Support Vector Machine Classifier
- [ ] W5.3 — Hyperparameter Tuning (Grid/Random/Optuna)
- [ ] W6.1 — PCA for Dimensionality Reduction
- [ ] W6.2 — TF-IDF + Text Classifier
- [ ] W6.3 — XGBoost/LightGBM on a Kaggle Tabular Dataset
- [ ] W6.4 — SMOTE for Imbalanced Classification
- [ ] W7.1 — MLP from Scratch (NumPy, MNIST)
- [ ] W7.2 — CNN on Fashion-MNIST
- [ ] W7.3 — Model Interpretability (SHAP / Feature Importance)
- [ ] W8.1 — Time Series Forecasting (ARIMA/Prophet)
- [ ] W8.2 — Anomaly Detection (Isolation Forest / Autoencoder)
- [ ] W8.3 — Full sklearn Pipeline (preprocessing + model + tuning)
- [ ] W8.4 — A/B Test Analysis

### Week 9–12: Hard

- [ ] W9.1 — Neural Network from Scratch (full backprop engine)
- [ ] W9.2 — CNN Architecture from Scratch (manual conv/pooling)
- [ ] W9.3 — RNN/LSTM for Sequence Prediction
- [ ] W10.1 — Attention Mechanism / Mini-Transformer from Scratch
- [ ] W10.2 — Fine-tune a Pretrained Transformer (BERT/DistilBERT)
- [ ] W10.3 — Build a Simple GAN
- [ ] W10.4 — Autoencoder / VAE
- [ ] W11.1 — Reinforcement Learning: Q-Learning Agent
- [ ] W11.2 — Transfer Learning for Image Classification
- [ ] W11.3 — Kaggle Competition Deep Dive
- [ ] W12.1 — End-to-End ML Deployment (FastAPI + Docker)
- [ ] W12.2 — Model Compression (Quantization/Pruning)
- [ ] W12.3 — Custom Loss Function / Optimizer
- [ ] W12.4 — Capstone Project

See [`ROADMAP.md`](ROADMAP.md) for a description, dataset suggestion, and difficulty note for every item above.
