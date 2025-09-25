import streamlit as st
import pandas as pd
import joblib

# Load the trained model
try:
    model = joblib.load('churn_model.pkl')
except FileNotFoundError:
    st.error("Model file 'churn_model.pkl' not found.")
    st.stop()

st.title("Telecom Churn Prediction")
st.write("Fill in the customer details below to predict churn likelihood.")

# Input fields for all required features
account_length = st.number_input("Account Length", min_value=0)
voice_mail_plan = st.selectbox("Voice Mail Plan", ["Yes", "No"])
voice_mail_messages = st.number_input("Voice Mail Messages", min_value=0)
day_mins = st.number_input("Day Minutes", min_value=0.0)
evening_mins = st.number_input("Evening Minutes", min_value=0.0)
night_mins = st.number_input("Night Minutes", min_value=0.0)
international_mins = st.number_input("International Minutes", min_value=0.0)
day_calls = st.number_input("Day Calls", min_value=0)
evening_calls = st.number_input("Evening Calls", min_value=0)
night_calls = st.number_input("Night Calls", min_value=0)
international_calls = st.number_input("International Calls", min_value=0)
total_charge = st.number_input("Total Charge", min_value=0.0)
total_calls = st.number_input("Total Calls", min_value=0)
total_minutes = st.number_input("Total Minutes", min_value=0.0)
charge_per_minute = st.number_input("Charge per Minute", min_value=0.0)
customer_service_calls = st.number_input("Customer Service Calls", min_value=0)
international_plan = st.selectbox("International Plan", ["Yes", "No"])
support_intensity = st.number_input("Support Intensity", min_value=0.0)
high_day_usage = st.selectbox("High Day Usage", ["Yes", "No"])
frequent_support = st.selectbox("Frequent Support", ["Yes", "No"])
premium_user = st.selectbox("Premium User", ["Yes", "No"])
log_total_charge = st.number_input("Log Total Charge", min_value=0.0)
log_customer_service_calls = st.number_input("Log Customer Service Calls", min_value=0.0)

# Prepare input data
input_data = pd.DataFrame({
    'account_length': [account_length],
    'voice_mail_plan': [1 if voice_mail_plan == "Yes" else 0],
    'voice_mail_messages': [voice_mail_messages],
    'day_mins': [day_mins],
    'evening_mins': [evening_mins],
    'night_mins': [night_mins],
    'international_mins': [international_mins],
    'customer_service_calls': [customer_service_calls],
    'international_plan': [1 if international_plan == "Yes" else 0],
    'day_calls': [day_calls],
    'evening_calls': [evening_calls],
    'night_calls': [night_calls],
    'international_calls': [international_calls],
    'total_charge': [total_charge],
    'total_calls': [total_calls],
    'total_minutes': [total_minutes],
    'charge_per_minute': [charge_per_minute],
    'support_intensity': [support_intensity],
    'high_day_usage': [1 if high_day_usage == "Yes" else 0],
    'frequent_support': [1 if frequent_support == "Yes" else 0],
    'premium_user': [1 if premium_user == "Yes" else 0],
    'log_total_charge': [log_total_charge],
    'log_customer_service_calls': [log_customer_service_calls]
})

# Predict
if st.button("Predict Churn"):
    prediction = model.predict(input_data)[0]
    result = "Likely to Churn" if prediction == 1 else "✅ Not Likely to Churn"
    st.success(f"Prediction: {result}")
