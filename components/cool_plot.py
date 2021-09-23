import streamlit as st
import pandas as pd
from utils.constants import API_URL


def main():
    # Maybe declare this 'extra' path somewhere...
    df_main = pd.read_csv(API_URL + 'COVID-19_Infectieradar_symptomen_per_dag.csv', delimiter=';')
    st.title('COVID-19 Dashboard')
    st.write("Here's our first attempt at using data to create a table:")
    st.write(df_main)