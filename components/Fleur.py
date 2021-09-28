from urllib.request import urlopen
import json
import pandas as pd
import plotly.express as px
import streamlit as st

import components.base as gSlider


def reproG():
    url= 'https://data.rivm.nl/covid-19/COVID-19_reproductiegetal.json'
    response = urlopen(url)
    json_data = json.loads(response.read())

    df = pd.DataFrame.from_dict(json_data)
    df['Date'] = pd.to_datetime(df['Date'])
    df2= df.astype({'Rt_low': 'float64','Rt_avg': 'float64','Rt_up': 'float64'})

    df2 = df2.set_index("Date")[gSlider.start_h: gSlider.end_h]
    min, max = df2.index.min().date(), df2.index.max().date()
    periode = str("<br>over periode: " + str(min) + " tot " + str(max))

    # reset to make sure nothing else is changed
    df2 = df2.reset_index()

    fig = px.line(data_frame=df2,
                  x='Date',
                  y=['Rt_low', 'Rt_avg', 'Rt_up'],
                  title= 'Reproductiegetal per dag' + periode,
                  width=500, height=300
                 )

    # axis updates
    fig.update_layout({'xaxis': {'title': {'text': 'Datum'}},
                      'yaxis': {'title': {'text': 'Reproductie getal'}}})


    st.write(fig)