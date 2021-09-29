from utils.helpers import write_meta
import pandas as pd
import plotly.express as px
import streamlit as st
import components.base as gSlider


def reproduction_plot():
    df = write_meta('COVID-19_reproductiegetal.json', json=True)
    df['Date'] = pd.to_datetime(df['Date'])

    df = df.set_index("Date")[gSlider.start_h: gSlider.end_h]
    min, max = df.index.min().date(), df.index.max().date()
    periode = str("<br>over periode: " + str(min) + " tot " + str(max))

    # Reset to make sure nothing else is changed
    df = df.reset_index()

    fig = px.line(data_frame=df,
                  x='Date',
                  y=['Rt_low', 'Rt_avg', 'Rt_up'],
                  title= 'Reproductiegetal per dag' + periode,
                  labels={"variable": "Legenda"},
                  width=500, height=400
                 )
    fig.data[0].name = "Ondergrens"
    fig.data[1].name = "Gemiddelde"
    fig.data[2].name = "Bovengrens"

    # Axis updates
    fig.update_layout({'xaxis': {'title': {'text': 'Datum'}},
                      'yaxis': {'title': {'text': 'Reproductie getal'}}})

    st.plotly_chart(fig, use_container_width=True)
