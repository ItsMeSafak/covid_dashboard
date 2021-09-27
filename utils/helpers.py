import pandas as pd
import streamlit as st
from utils.constants import API_URL

@st.cache
def load_data(url, index=None, dates=False):
    return pd.read_csv(API_URL + url, delimiter=';', index_col=index, parse_dates=[dates])