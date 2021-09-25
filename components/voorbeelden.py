import streamlit as st
import pandas as pd
from utils.constants import API_URL

#checkbox
check_box = st.checkbox('click me')
if check_box:
    st.write(df_ic)

# slider
values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)


import datetime
# date selector
begin, end = (1, 1)
begin, end = st.date_input("date range without default", [datetime.date(2019, 7, 6), datetime.date(2019, 7, 8)])
st.write(begin, end)

# dropdown selector
regio = st.selectbox('Selecteer een regio om de test data te bekijken.', df_testen["Security_region_name"].unique())
st.write(regio) #regio bevat een string met de geselecteerde optie

import plotly.express as px
# plotly figuur
fig = px.line(data_regio, x="Date_of_statistics", y=["Tested_with_result", "Tested_positive"], title="testen")
st.write(fig)