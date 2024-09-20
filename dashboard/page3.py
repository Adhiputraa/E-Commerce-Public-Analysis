import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    st.title("Question 3")
    df = pd.read_csv("data/completed.csv")
    st.write("### What column has the best correlation value with review_score?")
    st.write(" ")
    numerical_features = df.select_dtypes(['float','int'])
    corr_matrix = numerical_features.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Correlation heatmap')
    st.markdown(
            """
            ### Explanation 👈
            based on the values ​​in the correlation table, the one with the largest correlation value is `order_item_id` but the value is negative, which means the opposite
        """
        )
    st.write("#### This Visualization! 👈")
    st.pyplot(plt)
