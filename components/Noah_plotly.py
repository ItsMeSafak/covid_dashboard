import pandas as pd
import plotly.express as px
import streamlit as st

from utils.constants import API_URL


def testen():
    df_testen = pd.read_csv(API_URL + 'COVID-19_uitgevoerde_testen.csv', delimiter=';', parse_dates=["Date_of_statistics"])

    regio = st.selectbox('Selecteer een regio om de test data te bekijken.', df_testen["Security_region_name"].unique())
    data_regio = (df_testen[df_testen["Security_region_name"] == regio].dropna().set_index("Date_of_statistics"))

    start, end = (data_regio.index.min().date(), data_regio.index.max().date())

    # slider
    values = st.slider('Select a range of values', start, end, (start,end))
    selected_range_fig = data_regio[values[0]:values[1]].reset_index()

    #date selector
    #start_s, end_s = start, end
    #start_s, end_s = st.date_input("Selecteer een periode", [start, end])
    #selected_range_fig = data_regio[start_s:end_s].reset_index()

    # plotly figuur
    fig = px.line(selected_range_fig, x="Date_of_statistics", y=["Tested_with_result", "Tested_positive"],
                  title="Afgenomen testen / positieve uitslagen", labels={"Date_of_statistics": 'Datum', "value": "Aantal testen", "variable": "Data", "Tested_with_result": "test"})

    fig.data[0].name = "Afgenomen testen <br> met resultaat"
    fig.data[1].name = "Afgenomen testen <br> met positief resultaat"
    st.write(fig)


def ic():
    df_ic = pd.read_csv(API_URL + 'COVID-19_ic_opnames.csv ', delimiter=';', parse_dates=["Date_of_statistics"], index_col="Date_of_statistics")

    start, end = (df_ic.index.min().date(), df_ic.index.max().date())

    #slider
    start_s, end_s = st.slider("Selecteer een periode", start, end, (start,end))
    selected_range_fig = df_ic[start_s:end_s].reset_index()

    #date selector
    #start_s, end_s = start, end
    #start_s, end_s = st.date_input("Selecteer een periode", [start, end])
    #selected_range_fig = df_ic[start_s:end_s].reset_index()

    # plotly figuur
    fig = px.line(selected_range_fig, x="Date_of_statistics", y="IC_admission", title="Landelijke IC Opnames", labels={"Date_of_statistics": 'Datum',
                "IC_admission": "Aantal IC Opnames"})
    st.write(fig)



def riool():
    df_riool = pd.read_csv(API_URL + 'COVID-19_rioolwaterdata.csv', delimiter=';', parse_dates=["Date_measurement"])
    df_gemeente = df_riool.set_index("RWZI_AWZI_name")

    # laat riool df zien
    #riool_cb = st.checkbox('Show Riool dataframe')
    #if riool_cb:
    #    st.write(df_gemeente.sort_index(level=['RWZI_AWZI_name'], ascending=[True]))

    # kies de waarde
    data_switch = st.checkbox("ml aan/uit")
    if data_switch:
        ml = ("RNA_per_ml", "RNA per ml")
    else:
        ml = ("RNA_flow_per_100000", "RNA flow per 100000")

    # stad selectie bar/menu
    stad = st.selectbox('Selecteer een stad om de riooldata te bekijken.', df_riool["RWZI_AWZI_name"].unique())
    data_stad = (df_riool[df_riool["RWZI_AWZI_name"] == stad].set_index("Date_measurement")[ml[0]].sort_index()).dropna()


    #slider
    start, end = (data_stad.index.min().date(), data_stad.index.max().date())
    start_s, end_s = st.slider("Selecteer een periode", start, end, (start,end))
    selected_range_fig = data_stad[start_s:end_s].reset_index()

    fig = px.line(selected_range_fig, x="Date_measurement", y=ml[0], title="Riool", labels={'Date_measurement': 'Datum',
                ml[0]: ml[1]})
    st.write(fig)

    # bij de stad horende dataframe
    #data_stad_cb = st.checkbox('Laat het bijbehorende dataframe zien')
    #if data_stad_cb:
    #    st.write(data_stad)