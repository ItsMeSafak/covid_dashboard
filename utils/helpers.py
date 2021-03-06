import pandas as pd
import streamlit as st
from utils.constants import API_URL


def load_data(url, index=None, dates=False, json=False, local=False):
    if ('COVID-19' in url):
        meta_data = url[:-3] + 'html'
        if (json): 
            meta_data = meta_data[:-5] + 'html'
        st.markdown("*Referentie: " + API_URL + meta_data + "*")
    return write_meta(url, index, dates, json, local)

@st.cache
def write_meta(url, index=None, dates=False, json=False, local=False):
    if (json):
        if ('COVID-19' in url):
            return pd.read_json(API_URL + url)
        return pd.read_json(url)
    else:
        if (local):
            return pd.read_csv('data/' + url, delimiter=';', index_col=index, parse_dates=[dates])
        return pd.read_csv(API_URL + url, delimiter=';', index_col=index, parse_dates=[dates])
