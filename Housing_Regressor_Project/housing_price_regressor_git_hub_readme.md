# 🏠 Housing Price Regressor

> 🔍 An end-to-end regression-based machine learning project for predicting housing prices with model comparison and Flask deployment.

---

## 📌 Overview

This project develops and evaluates a range of regression models for housing price prediction based on area-level economic, demographic, and property features, covering the full ML pipeline from preprocessing to Flask-based deployment.

---

## 📊 Dataset

- **File:** `USA_Housing.csv`
- **Target Variable:** `Price`
- **Features:**
  - Avg. Area Income
  - Avg. Area House Age
  - Avg. Area Number of Rooms
  - Avg. Area Number of Bedrooms
  - Area Population

---

## 🧹 Data Preprocessing

- Missing value checks
- Feature scaling for linear & distance-based models
- Train-test split

---

## 🧠 Models Implemented

- Linear Regression
- Robust Regression
- Ridge Regression
- Lasso Regression
- Elastic Net
- Polynomial Regression
- SGD Regressor
- Artificial Neural Network (ANN)
- Random Forest Regressor
- Support Vector Machine (SVM)
- LightGBM (LGBM)
- XGBoost Regressor
- K-Nearest Neighbors (KNN)

All trained models are serialized using **Pickle**.

---

## 📈 Model Evaluation

Evaluation metrics used:

- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

A comparative performance table is saved as:

```
model_evaluation_results.csv
```

This table is also displayed in the web application.

---

## 🌐 Flask Web Application

The web app allows users to:

- Select a regression model
- Enter housing feature values
- Predict house prices instantly
- View model comparison results

---

## 🚀 How to Run Locally

### 1️⃣ Clone the Repository

```
https://github.com/ronitadas05/6months-AI-roadmap_2025/tree/main/Housing_Regressor_Project
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```
python app.py
```



---

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost, LightGBM
- Flask
- HTML / CSS

---

## 📌 Key Learnings

- End-to-end ML pipeline development
- Regression model comparison
- Model serialization & reuse
- Integrating ML models with Flask
- Structuring ML projects for GitHub

---

## 🔮 Future Enhancements

- Hyperparameter tuning&#x20;
- Model explainability&#x20;
- Cloud deployment

---

## 👤 Author

**Ronita Das**



