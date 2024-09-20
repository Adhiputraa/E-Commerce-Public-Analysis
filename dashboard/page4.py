import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    st.title("Question 4")
    df = pd.read_csv("data/completed.csv")
    st.write("### What is the average time taken from order completion to review creation (order_delivered_customer_date to review_creation_date)?")

    st.write(" ")
    # change object to datetime
    df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'], errors='coerce')
    df['review_creation_date'] = pd.to_datetime(df['review_creation_date'], errors='coerce')

    # create new column
    df['time_to_review_days'] = (df['review_creation_date'] - df['order_delivered_customer_date']).dt.days

    # count  average time dari from order delivered to review creation
    average_time_to_review = df['time_to_review_days'].mean()
    df = df[df['time_to_review_days'] >= 0]
    average_time_to_review = df['time_to_review_days'].mean() 
    st.write(f"Average time taken from order completion to review creation: {average_time_to_review:.2f} days")
    st.write("**Explaination, based on calculations that the average customer makes a review after **3.6 hours** after their order is completed 👈**")
