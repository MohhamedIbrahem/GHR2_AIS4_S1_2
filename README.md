
# 🏥 Healthcare Billing Amount Prediction

This repository contains a machine learning model that predicts the **billing amount** for a patient based on their medical and demographic attributes. The goal is to support healthcare providers and insurers in forecasting patient costs, optimizing resources, and understanding cost drivers.

## 📌 Project Overview

Medical billing can be influenced by factors such as age, medical condition, insurance provider, and test results. This project uses a supervised machine learning model to estimate the **expected billing amount** for a patient based on historical data.

## 🧾 Dataset Features

The dataset includes **55,500 patient records** with the following columns:

| Feature | Description |
|--------|-------------|
| `Age` | Patient's age |
| `Gender` | Male / Female |
| `Blood Type` | Patient's blood group |
| `Medical Condition` | Primary diagnosis (e.g., Cancer, Diabetes, Obesity) |
| `Date of Admission` | Admission date |
| `Doctor` | Attending physician |
| `Hospital` | Hospital or facility name |
| `Insurance Provider` | Patient’s insurance (e.g., Medicare, Aetna) |
| `Room Number` | Room number during stay |
| `Admission Type` | Elective, Emergency, Urgent |
| `Discharge Date` | Date of discharge |
| `Medication` | Prescribed medication |
| `Test Results` | Lab test results (Normal, Abnormal, Inconclusive) |
| `Billing Amount` | 💰 Target variable to predict |

## 🧠 Model

- **Task**: Regression (predicting a continuous value)
- **Target**: `Billing Amount`
- **Models used**: (e.g., Linear Regression, XGBoost, Random Forest)
- **Evaluation metrics**: MAE, RMSE, R²

## 🛠️ Technologies

- Python, Pandas, NumPy
- Scikit-learn / XGBoost
- Streamlit (for API deployment)
- Matplotlib / Seaborn (for visualization)

## 📁 Project Structure

```
.
├── app/                  # Web API using Streamlit
├── data/                 # Original and processed datasets
├── models/               # Saved machine learning models
├── notebooks/            # EDA and model training notebooks
├── requirements.txt      # Python dependencies
├── README.md             # Documentation
└── streamlit_app.py               # API main entry point
```

## ▶️ Example Usage (API)

**POST** `/predict`  
**Input JSON:**

```json
{
  "Age": 45,
  "Gender": "Female",
  "Blood Type": "O+",
  "Medical Condition": "Diabetes",
  "Insurance Provider": "Medicare",
  "Admission Type": "Urgent",
  "Test Results": "Normal"
}
```

**Output:**

```json
{
  "predicted_billing_amount": 18750.63
}
```

## 📉 Evaluation

Evaluation results, feature importance, and error distributions are provided in the `notebooks/` folder.




