import streamlit as st
import pandas as pd
import pickle

# Load the model
with open("D:\mohamed\ML_Task\Healthcare\BillingAmountPrediction.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="Billing Predictor", page_icon="💰")
st.title("💡 Predict Patient Billing Amount")

st.markdown("Enter the following patient details:")

# --- INPUT FIELDS ---

age = st.number_input("Age", min_value=0, max_value=120, value=30)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
medical_condition = st.selectbox("Medical Condition", ['Cancer', 'Obesity', 'Diabetes', 'Asthma', 'Hypertension','Arthritis'])
insurance_provider = st.selectbox("Insurance Provider",['Blue Cross', 'Medicare', 'Aetna', 'UnitedHealthcare', 'Cigna'])
admission_type = st.selectbox("Admission Type",['Urgent', 'Emergency', 'Elective'])
medication = st.selectbox("Medication",['Paracetamol', 'Ibuprofen', 'Aspirin', 'Penicillin', 'Lipitor'])
test_results =  st.selectbox("Test Results",['Normal', 'Inconclusive', 'Abnormal'])

# --- ENCODING MAPS ---
gender_map = {"Male": 0, "Female": 1}
condition_map = {"Cancer": 0, "Obesity": 1, "Diabetes": 2, "Asthma": 3,"Hypertension": 4,"Arthritis": 5}
insurance_map = {"Blue Cross": 0, "Medicare": 1, "Aetna": 2, "UnitedHealthcare": 3,"Cigna": 4}
admission_map = {"Emergency": 0, "Elective": 1, "Urgent": 2, "Elective": 3}
medication_map = {"Paracetamol": 0, "Aspirin": 1, "Ibuprofen": 2, "Penicillin": 3,"Lipitor": 4}
results_map = {"Normal": 0, "Inconclusive": 1, "Abnormal": 2}

# --- BUTTON ---
if st.button("🔍 Predict Billing Amount"):
    try:
        input_data = pd.DataFrame([{
            "Age": age,
            "Gender": gender_map[gender],
            "Medical Condition": condition_map[medical_condition],
            "Insurance Provider": insurance_map[insurance_provider],
            "Admission Type": admission_map[admission_type],
            "Medication": medication_map[medication],
            "Test Results": results_map[test_results]
        }])

        prediction = model.predict(input_data)[0]
        st.success(f"💰 Estimated Billing Amount: ₹{prediction:,.2f}")
    except Exception as e:
        st.error(f"⚠️ Prediction failed: {e}")


# streamlit run streamlit_app.py


