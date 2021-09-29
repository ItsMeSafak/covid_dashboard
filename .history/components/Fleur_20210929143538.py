from utils.helpers import load_data
import pandas as pd
import plotly.express as px
import streamlit as st
import components.base as gSlider


def reproG():
    url= 'COVID-19_reproductiegetal.json'
    df = load_data(url, json=True)
    print(df.head())
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
                  labels={"variable": "Legenda"},
                  width=500, height=400
                 )
    fig.data[0].name = "Ondergrens"
    fig.data[1].name = "Gemiddelde"
    fig.data[2].name = "Bovengrens"

    # axis updates
    fig.update_layout({'xaxis': {'title': {'text': 'Datum'}},
                      'yaxis': {'title': {'text': 'Reproductie getal'}}})

    st.plotly_chart(fig, use_container_width=True)
