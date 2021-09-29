import pandas as pd
import streamlit as st
from utils.constants import API_URL

def load_data(url, index=None, dates=False):
    meta_data = url[:-3] + 'html'
    st.markdown("*Referentie: " + API_URL + meta_data + "*")
    return write_meta(url, index, dates)

@st.cache
def write_meta(url, index=None, dates=False):
    return pd.read_csv(API_URL + url, delimiter=';', index_col=index, parse_dates=[dates])