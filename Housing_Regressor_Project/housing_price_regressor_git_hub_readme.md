# 🏠 Housing Price Regressor

> 🔍 End-to-end machine learning project for predicting housing prices using multiple regression models with a Flask-based web application.

---

## 📌 Overview
This project builds and compares a wide range of **regression models** to predict housing prices based on socio-economic and housing features. It covers the complete ML lifecycle—from data preprocessing and model training to evaluation and **real-time deployment using Flask**.

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
- Deployment-ready input pipeline

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

### Main Routes
- `/` – Home page
- `/predict` – Prediction endpoint
- `/results` – Model evaluation table

---

## 🚀 How to Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/housing-price-regressor.git
cd housing-price-regressor
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application
```bash
python app.py
```

Open your browser at:
```
http://127.0.0.1:5000/
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
- Hyperparameter tuning (GridSearchCV / Optuna)
- Model explainability (SHAP)
- Dockerization
- Cloud deployment
- CI/CD integration

---

## 👤 Author
**Ronieta Das**  
Machine Learning & Data Science Enthusiast

---

⭐ If you find this project useful, don’t forget to give it a star!

