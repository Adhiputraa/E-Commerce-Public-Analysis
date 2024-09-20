#Importing library
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import page1
import page2
import page3
import page4

# Set global page configuration
st.set_page_config(page_title="Dashboard", layout="wide", initial_sidebar_state="expanded")

# Create a sidebar with a header
st.sidebar.title("# Welcome to my Dashboard! 👋")
st.sidebar.header("Home")
st.markdown(
            """
            # Brazilian Ecommerce Analysis
            This dataset was generously provided by Olist, the largest department store in Brazilian marketplaces.

            Olist connects small businesses from all over Brazil to channels without hassle and with a single contract.
        
            Those merchants are able to sell their products through the Olist Store and ship them directly to the customers using Olist logistics partners.
        
            See more on our website: www.olist.com

            **👈 Select a features to looking out the visualization and explanation from the dropdown on the left**

            ### Want to information more?

            - Check out the full dataset [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) 
            - Jump into our github [repositories](https://github.com/Adhiputraa?tab=repositories)

            ### Want to connect with me?

            - You can contact me to my linkedin profile [Linkedin](https://www.linkedin.com/in/aditya-yoga-a-8316a1129/)
            - Come and enjoy my another data viz on my tableau profil [Tableau](https://public.tableau.com/app/profile/aditya.yoga.adhiputra5161/vizzes)
        """
        )

# Sidebar select button for page navigation
page = st.sidebar.selectbox("Go to", ["Question 1","Question 2","Question 3","Question 4"])

# Display the selected page
if page == "Question 1":
    page1.app()
if page == "Question 2":
    page2.app()
if page == "Question 3":
    page3.app()
if page == "Question 4":
    page4.app()
