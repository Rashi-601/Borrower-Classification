import streamlit as st
import joblib
import pandas as pd

# Load the combined pipeline
combined_pipeline = joblib.load('combined_pipeline.pkl')

# Define the input form
st.title("Loan Prediction")
st.write("Enter the loan details below:")

loan_tenure = st.number_input("Loan Tenure", min_value=0)
borrower_apr = st.number_input("Borrower APR", min_value=0.0, format="%.4f")
loan_first_defaulted_cycle_number = st.number_input("Loan First Defaulted Cycle Number", min_value=0)
monthly_loan_payment = st.number_input("Monthly Loan Payment", min_value=0.0, format="%.2f")
stated_monthly_income = st.number_input("Stated Monthly Income", min_value=0.0, format="%.2f")
lp_customer_payments = st.number_input("LP Customer Payments", min_value=0.0, format="%.2f")
total_amount = st.number_input("Total Amount", min_value=0.0, format="%.2f")
lp_net_principal_loss = st.number_input("LP Net Principal Loss", min_value=0.0, format="%.2f")
lp_customer_principal_payments = st.number_input("LP Customer Principal Payments", min_value=0.0, format="%.2f")
prosper_rating = st.text_input("Prosper Rating (Alpha)")
interest_amount = st.number_input("Interest Amount", min_value=0.0, format="%.2f")
lp_gross_principal_loss = st.number_input("LP Gross Principal Loss", min_value=0.0, format="%.2f")
loan_current_days_delinquent = st.number_input("Loan Current Days Delinquent", min_value=0)

# Input data as a dictionary
input_data = {
    'LoanTenure': loan_tenure,
    'BorrowerAPR': borrower_apr,
    'LoanFirstDefaultedCycleNumber': loan_first_defaulted_cycle_number,
    'MonthlyLoanPayment': monthly_loan_payment,
    'StatedMonthlyIncome': stated_monthly_income,
    'LP_CustomerPayments': lp_customer_payments,
    'TotalAmount': total_amount,
    'LP_NetPrincipalLoss': lp_net_principal_loss,
    'LP_CustomerPrincipalPayments': lp_customer_principal_payments,
    'ProsperRating (Alpha)': prosper_rating,
    'InterestAmount': interest_amount,
    'LP_GrossPrincipalLoss': lp_gross_principal_loss,
    'LoanCurrentDaysDelinquent': loan_current_days_delinquent,
}

# Convert input data to DataFrame
input_df = pd.DataFrame([input_data])

# Prediction
if st.button("Predict"):
    predictions = combined_pipeline.predict(input_df)
    st.write("Predictions:")
    st.write(f"EMI: {predictions[0][0]}")
    st.write(f"ELA: {predictions[0][1]}")
    st.write(f"PROI: {predictions[0][2]}")
