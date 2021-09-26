import pandas as pd
import plotly.express as px
import streamlit as st

from utils.constants import API_URL


def riool():
    df_ziekenhuis_opnames = pd.read_csv(API_URL + 'COVID-19_ziekenhuis_ic_opnames_per_leeftijdsgroep.csv ',
                           delimiter=';')

    df_ziekenhuis_opnames.head()
