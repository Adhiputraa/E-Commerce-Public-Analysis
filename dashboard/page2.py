import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    st.title("Question 2")
    df = pd.read_csv("data/completed.csv")
    st.write("### What is the total transaction value (payment_value) based on the payment method?")
    st.write(" ")
    
    st.markdown(
            """
            ### Explanation 👈
            Based on the table, people prefer transactions using credit cards. This can be seen from the fact that the largest transaction value is in the credit card payment type
        """
        )
    total_transaction = df.groupby('payment_type').agg({
    'transaction_value' : 'sum'
    })

    st.write("#### This table showing the `payment_method` with the highest transaction! 👈")
    st.write(total_transaction)