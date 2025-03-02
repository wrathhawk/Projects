import streamlit as st
import pickle
import pandas as pd

# Načtení uloženého modelu (předtím ho musíš uložit pomocí pickle)
with open("Bank_Churn/churn_pipeline.pkl", "rb") as file:
    model = pickle.load(file)

# UI aplikace
st.title("Customer Churn Prediction")

# Vstupy od uživatele
credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=600)
age = st.number_input("Age", min_value=18, max_value=100, value=30)
tenure = st.number_input("Tenure", min_value = 0, max_value = 10, value=3)
balance = st.number_input("Balance on account", min_value=0, value=50000)
products_number = st.number_input("Number of products that customer has", min_value=1, value=1)
credit_card = st.number_input("Does customer have credit card? (input 0 for NO and 1 for YES)", min_value=0, max_value=1, value=0)
active_member = st.number_input("Is the customer active member? (input 0 for NO and 1 for YES)", min_value=0, max_value=1, value=0)
estimated_salary = st.number_input("Estimated salary of the customer", min_value=0, value=30000)

# Předpověď
if st.button("Predict"):
    input_data = pd.DataFrame([[credit_score, age, tenure, balance, products_number, credit_card, active_member, estimated_salary]], columns=["credit_score", "age", "tenure", "balance", "products_number", "credit_card", "active_member", "estimated_salary"])
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.error("🚨 Zákazník pravděpodobně odejde!")
    else:
        st.success("✅ Zákazník pravděpodobně zůstane.")
