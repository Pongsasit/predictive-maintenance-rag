import os
import requests
import json

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

from dotenv import load_dotenv

from function import check_password
from config import watsonx_assistant_html, visualizaer_url

load_dotenv()
# BE_ENDPOINT = os.environ["BE_ENDPOINT"]
# CLIENT_USERNAME = os.environ["CLIENT_USERNAME"]
# CLIENT_PASSWORD = os.environ["CLIENT_PASSWORD"]

if 'hide' not in st.session_state:
    st.session_state.hide = False
def show_hide():
    st.session_state.hide = not st.session_state.hide

# Configure Streamlit page layout
st.set_page_config(layout="wide")

st.title("Business Partner Usecase Example: Predictive Maintenance")

# Create two columns for chat interface and data visualization
visualize_column, chat_column = st.columns(2)

# Create a mock dataframe
data = {
    "Device ID": ["AA01", "AA02", "BB02", "CC01", "DD03"],
    "Device Type": ["A", "A", "B", "C", "D"],
    "Status": ["READY", "FAILED", "READY", "READY", "READY"],
    "Predicted Status": ["READY", "FAILED", "RISK", "READY", "READY"]
}
df = pd.DataFrame(data)

# Define a function to color entire rows based on status

def color_status(val):
    if val == "READY":
        color = 'color: green'
    elif val == "RISK":
        color = 'color: orange'
    else:
        color = 'color: red'
    return color

# Apply the function to the 'Status' column
styled_df = df.style.applymap(color_status, subset=['Status', 'Predicted Status'])
# Function to toggle the dashboard visibility
def show_hide():
    st.session_state.hide = not st.session_state.hide

# Data visualization dashboard
with visualize_column:
    st.title("VISUALIZE")
    st.button('Show Dashboard', on_click=show_hide)
    if st.session_state.hide:
        with st.container():
            st.dataframe(styled_df, height=225, width=1200)

with chat_column:
    # st.title("CHAT")
    components.html(watsonx_assistant_html, height=600)