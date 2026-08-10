import streamlit as st
import pandas as pd
from io import StringIO
import json
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


login_option =st.sidebar.radio('Login/SignUp', ['Login', 'SignUp'])


if login_option == 'Login':
    with st.sidebar.form("Login"):
        st.write("Login Here:")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Login")
        if submitted:
            pass
else:
    with st.sidebar.form("SignUp"):
        st.write("SignUp Here:")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        email = st.text_input("Email")

        # Every form must have a submit button.
        submitted = st.form_submit_button("SignUp")
        if submitted:
            pass



banner = Image.open('./data/banner8.png')
st.image(banner)

st.title(":zap: Dashboard")
st.text("Welcome to the dashboard!")


col1, col2= st.columns(2)
col1.metric(label="Website Members", value=4000, delta=12)
col2.metric(label="Telegram Members", value=4000, delta=12)



with st.expander("Statistics"):
    # st.pyplot(sns.histplot(np.random.randn(100)))
    fig, ax = plt.subplots()
    sns.histplot(np.random.randn(100), ax=ax)
    st.pyplot(fig)


with st.expander("User Profile"):
    col1, col2 = st.columns(2)
    col1.text_input("Name:")
    col2.text_input("Location:")
    # st.camera_input('camera input' , key='camera_input')

