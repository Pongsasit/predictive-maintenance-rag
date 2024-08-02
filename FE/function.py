import os
import requests
import json

import pandas as pd
import streamlit as st

from dotenv import load_dotenv

load_dotenv()
BE_ENDPOINT = ''#os.environ["BE_ENDPOINT"]
CLIENT_USERNAME = ''#os.environ["CLIENT_USERNAME"]
CLIENT_PASSWORD = ''#os.environ["CLIENT_PASSWORD"]

def check_password(CLIENT_USERNAME, CLIENT_PASSWORD):
    """Returns `True` if the user had a correct password."""

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.selectbox(
                'Your Role: ',
                ('Traffic Analyst', 'Data Analyst'), key="role")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if str(st.session_state["username"]) == str(CLIENT_USERNAME) and str(st.session_state["password"]) == str(CLIENT_PASSWORD):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the username or password.
            del st.session_state["username"]
            if str(st.session_state["role"]) == str('Traffic Analyst'):
                st.session_state["selected_role"] = 'gate'
            else:
                st.session_state["selected_role"] = 'finance'
        else:
            st.session_state["password_correct"] = False

    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return {'result':True, 'selected_role':st.session_state["selected_role"]}

    # Show inputs for username + password.
    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return {'result':False, 'selected_role':st.session_state["selected_role"]}