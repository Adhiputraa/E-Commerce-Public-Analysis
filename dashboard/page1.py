import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    df = pd.read_csv("data/completed.csv")
    top_10 = df['customer_city'].value_counts().head(10)
    plt.figure(figsize=(12, 8))

    st.title("Question 1")
    st.write("### Which 10 cities/provinces have the highest number of customers?")
    st.write(" ")
    st.markdown(
            """
            ### Explanation 👈
            Based on the dataset, São Paulo and Rio de Janeiro are the top two cities with the highest number of customers, with São Paulo ranking first and Rio de Janeiro second.
            This observation aligns with data from World Population Review, which indicates that São Paulo is the largest city in Brazil with a population of approximately 22.8 million in 2024, while Rio de Janeiro follows with around 13.8 million residents [World Population Review](https://worldpopulationreview.com/cities/brazil)​.
            The high population density in these cities is reflected in their dominance in e-commerce transactions, as they house a large customer base, contributing significantly to Brazil's overall online marketplace activity.
        """
        )
    
    st.write("#### This table showing city with the highest number of customers! 👈")
    st.write(top_10)
    sns.barplot(x=top_10.values, y=top_10.index)
    plt.title('Top 10 Cities by Number of Customers')
    
    st.write("#### This Visualization! 👈")
    st.pyplot(plt)