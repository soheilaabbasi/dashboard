import streamlit as st
import pandas as pd
from io import StringIO
import json
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
import sys

#sys.path.append('.')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from db.models import Message

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


# Banner
banner = Image.open('./data/banner8.png')
st.image(banner)

st.title(":zap: Dashboard")
st.text("Welcome to the dashboard!")

# # Metrics
# col1, col2= st.columns(2)
# col1.metric(label="Website Members", value=4800, delta=12)
# col2.metric(label="Telegram Members", value=2102, delta=12)

# # Statistics
# with st.expander("Statistics"):
#     # st.pyplot(sns.histplot(np.random.randn(100)))
#     fig, ax = plt.subplots()
#     sns.histplot(np.random.randn(100), ax=ax)
#     st.pyplot(fig)


# Questions
with st.expander("Q / A"):
    query = st.text_input('Search:')

    # select top 10 from messages
    for msg in Message.objects.all().order_by('-date')[:100]:
        if not msg.text or msg.text[-1] not in '?؟':
            continue

        if query and query not in msg.text:
            continue

        col1, col2 = st.columns([1,4])
        col1.write(f'**{msg.user.username}**')
        if query:
            col2.markdown(msg.text.replace(query, f'**{query}**'))
        else:
            col2.write(msg.text)


        #col2.write(msg.text)

    st.button("Show More")

    col1, col2 = st.columns(2)
    col1.button('<Previous')
    col2.button('Next>')
# # User Info
# with st.expander("User Profile"):
#     col1, col2 = st.columns(2)
#     col1.text_input("Name:")
#     col2.text_input("Location:")
#     # st.camera_input('camera input' , key='camera_input')

