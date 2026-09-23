# Roadmap — 12 Weeks, Easy → Medium → Hard

Pace: **3–4 problems/week**. Each entry: what to build, a suggested dataset/source, and why it's in this slot.

---

## Weeks 1–4 · Easy (fundamentals)

**Week 1**
1. **Linear Regression from Scratch** — implement with NumPy only (no sklearn), predict housing prices. *Dataset: Boston/California housing.* Builds intuition for loss functions and gradient descent before using library shortcuts.
2. **Titanic Survival Classifier** — logistic regression with sklearn, basic feature encoding. *Dataset: Kaggle Titanic.*
3. **K-Nearest Neighbors from Scratch** — implement KNN manually, classify Iris. *Dataset: Iris.*

**Week 2**
1. **Decision Tree Classifier** — train with sklearn, visualize the tree, explain splits. *Dataset: Wine or Iris.*
2. **Data Cleaning & EDA Challenge** — take an intentionally messy dataset, handle missing values/outliers/dtypes. *Dataset: any raw Kaggle CSV.*
3. **Naive Bayes Spam Classifier** — bag-of-words + Naive Bayes. *Dataset: SMS Spam Collection.*
4. **K-Means Clustering from Scratch** — implement the algorithm manually, segment customers. *Dataset: Mall Customer Segmentation.*

**Week 3**
1. **Cross-Validation & Metrics Deep Dive** — compare k-fold vs. single train/test split; compute precision/recall/F1/ROC-AUC by hand once. *Dataset: any prior one.*
2. **Feature Engineering Practice** — polynomial/interaction features, scaling comparison (standard vs. min-max), measure impact on model accuracy.
3. **Simple Movie Recommender** — popularity-based baseline + basic user-based collaborative filtering. *Dataset: MovieLens 100k.*

**Week 4**
1. **Gradient Descent from Scratch** — implement batch and stochastic GD, plot convergence curves.
2. **Handling Imbalanced Data** — class weights + random oversampling on a skewed dataset. *Dataset: Credit Card Fraud (small sample).*
3. **Time Series Plotting & Moving Average Forecast** — EDA + naive/moving-average baseline forecast. *Dataset: any stock or weather series.*
4. **Confusion Matrix & ROC Curve Visualizer** — write a small reusable function/tool that takes y_true/y_pred and plots both.

---

## Weeks 5–8 · Medium (techniques)

**Week 5**
1. **Random Forest vs. Gradient Boosting Comparison** — same tabular dataset, compare accuracy/training time/feature importance.
2. **Support Vector Machine Classifier** — try linear vs. RBF kernel, visualize the decision boundary on 2D data.
3. **Hyperparameter Tuning** — GridSearchCV vs. RandomizedSearchCV vs. Optuna on the same model, compare tuning cost vs. gain.

**Week 6**
1. **PCA for Dimensionality Reduction** — reduce a high-dimensional dataset to 2D for visualization, then measure model performance with/without PCA.
2. **TF-IDF + Text Classifier** — sentiment or news-category classification. *Dataset: AG News or IMDB reviews.*
3. **XGBoost/LightGBM on a Kaggle Tabular Dataset** — pick an active or past competition, build a real submission pipeline.
4. **SMOTE for Imbalanced Classification** — apply SMOTE properly (inside CV folds, not before) on a fraud/churn dataset.

**Week 7**
1. **MLP from Scratch (NumPy)** — forward pass + manual backprop, no autograd. *Dataset: MNIST (subset).*
2. **CNN on Fashion-MNIST** — using PyTorch or TensorFlow this time (framework allowed).
3. **Model Interpretability** — SHAP values or permutation feature importance on one of your Week 5–6 models.

**Week 8**
1. **Time Series Forecasting** — ARIMA or Prophet on a real seasonal series, evaluate with a proper time-based split.
2. **Anomaly Detection** — Isolation Forest or a simple autoencoder reconstruction-error approach. *Dataset: sensor/IoT or fraud data.*
3. **Full sklearn Pipeline** — chain preprocessing + model + `GridSearchCV` into a single `Pipeline` object.
4. **A/B Test Analysis** — statistical significance testing (t-test/chi-square) on an experiment dataset, write up the decision.

---

## Weeks 9–12 · Hard (from-scratch & advanced)

**Week 9**
1. **Neural Network from Scratch — Full Backprop Engine** — build a tiny autograd-style library (layers, activations, backward pass) with no frameworks.
2. **CNN Architecture from Scratch** — implement convolution and pooling manually (no `nn.Conv2d`), test on a small image set.
3. **RNN/LSTM for Sequence Prediction** — character-level text generation or time-series prediction.

**Week 10**
1. **Attention Mechanism / Mini-Transformer from Scratch** — implement scaled dot-product attention and a minimal encoder block.
2. **Fine-tune a Pretrained Transformer** — BERT/DistilBERT via HuggingFace on a text classification task.
3. **Build a Simple GAN** — generator + discriminator on MNIST digits.
4. **Autoencoder / VAE** — for anomaly detection or generative sampling.

**Week 11**
1. **Reinforcement Learning: Q-Learning Agent** — solve a Gym environment (FrozenLake or CartPole).
2. **Transfer Learning for Image Classification** — fine-tune ResNet/EfficientNet on a small custom image dataset.
3. **Kaggle Competition Deep Dive** — pick one competition, build a genuinely competitive pipeline (feature engineering + ensembling), write up the leaderboard result.

**Week 12**
1. **End-to-End ML Deployment** — train a model, serve it via FastAPI, containerize with Docker, add a basic CI workflow.
2. **Model Compression** — quantize or prune a trained model, benchmark accuracy vs. speed/size tradeoff.
3. **Custom Loss Function / Optimizer** — implement something like focal loss or a custom optimizer in PyTorch from the underlying math.
4. **Capstone Project** — combine two or more techniques above into one polished, portfolio-quality project with a full write-up (this is the one to pin on your GitHub profile).

---

## Notes on pacing

- If a "hard" problem eats more than a week, that's fine — it's normal for Weeks 9–12 to run slower than Weeks 1–4. Better to slow down than skip the write-up.
- Swap datasets freely; the *skill* being practiced is what matters, not the exact dataset named here.
- Feel free to reorder within a week, but keep the week-to-week difficulty progression intact — it's what makes the repo read as a coherent learning arc to anyone browsing it.
