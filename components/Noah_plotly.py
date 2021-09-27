import pandas as pd
import plotly.express as px
import streamlit as st
from utils.constants import API_URL
from utils.helpers import load_data


def testen():
    df_testen = load_data('COVID-19_uitgevoerde_testen.csv',
                            "Date_of_statistics",
                            "Date_of_statistics").sort_index()

    regio = st.selectbox('Selecteer een regio om de test data te bekijken.',
                         sorted(df_testen["Security_region_name"].unique()))

    data_regio = (df_testen[df_testen["Security_region_name"] == regio].dropna())

    start, end = (data_regio.index.min().date(), data_regio.index.max().date())

    # slider
    start_s, end_s = st.slider("Selecteer een periode", start, end, (start, end))
    selected_range_fig = data_regio[start_s:end_s]

    # date selector
    # start_s, end_s = start, end
    # start_s, end_s = st.date_input("Selecteer een periode", [start, end])
    # selected_range_fig = data_regio[start_s:end_s]

    # plotly figuur
    fig = px.line(selected_range_fig, x=selected_range_fig.index, y=["Tested_with_result", "Tested_positive"],
                  title="Afgenomen testen met uitslag en positieve uitslagen: " + regio,
                  labels={"Date_of_statistics": 'Datum',
                          "value": "Aantal testen",
                          "variable": "Data",
                          "Tested_with_result": "test"})

    fig.data[0].name = "Afgenomen testen <br> met uitslag"
    fig.data[1].name = "Afgenomen testen <br> met positief resultaat"
    st.write(fig)

def ic():
    df_ic = load_data('COVID-19_ic_opnames.csv ',
                            "Date_of_statistics",
                            "Date_of_statistics").sort_index()
    # slice index range
    start, end = (df_ic.index.min().date(), df_ic.index.max().date())

    # slider
    start_s, end_s = st.slider("Selecteer een periode", start, end, (start, end))
    selected_range_fig = df_ic[start_s:end_s]

    # date selector
    # start_s, end_s = start, end
    # start_s, end_s = st.date_input("Selecteer een periode", [start, end])
    # selected_range_fig = df_ic[start_s:end_s]

    # plotly figuur
    fig = px.line(selected_range_fig, x=selected_range_fig.index, y="IC_admission",
                  title="Landelijke IC Opnames",
                  labels={"Date_of_statistics": 'Datum',
                          "IC_admission": "Aantal IC Opnames"})
    st.write(fig)

def riool():
    df_riool = load_data('COVID-19_rioolwaterdata.csv',
                            "Date_measurement",
                            "Date_measurement").sort_index()

    # kies rwzi
    rwzi = st.selectbox('Selecteer een stad om de riooldata te bekijken.', sorted(df_riool["RWZI_AWZI_name"].unique()))

    # kies de waarde "RNA_per_ml" of "RNA per ml"
    data_switch = st.checkbox("ml aan/uit")
    if data_switch:
        ml = ("RNA_per_ml", "RNA per ml")
    else:
        ml = ("RNA_flow_per_100000", "RNA flow per 100000")

    # stad selectie dataframe
    data_stad = df_riool[df_riool["RWZI_AWZI_name"] == rwzi][ml[0]].dropna().sort_index()
    if not(data_stad.empty or len(data_stad) <= 2):
        # slider periode
        start, end = (data_stad.index.min().date(), data_stad.index.max().date())
        start_s, end_s = st.slider("Selecteer een periode", start, end, (start, end))

        # slice dataframe
        selected_range_fig = data_stad[start_s:end_s]

        # plotly
        fig = px.line(selected_range_fig, x=selected_range_fig.index, y=ml[0],
                      title="Rioolwater data " + rwzi,
                      labels={'Date_measurement': 'Datum',
                              ml[0]: ml[1]}, markers="o")
        st.write(fig)
    else:
        st.write("Data ontbreekt voor selectie, deze data is aanwezig:")
        st.write(data_stad)


def Opname_overlijden():
    df = load_data('COVID-19_aantallen_gemeente_per_dag.csv',
                            "Date_of_publication",
                            "Date_of_publication").dropna()

    region = st.multiselect('Selecteer een regio om de test data te bekijken.',
                            sorted(df["Security_region_name"].unique()),
                            default=sorted(df["Security_region_name"].unique()) )

    df2 = df.loc[df["Security_region_name"].isin(region)]
    start, end = (df2.index.min().date(), df2.index.max().date())
    # slider
    start_s, end_s = st.slider("Selecteer een periode", start, end, (start, end))
    df2 = df2[start_s:end_s].groupby(["Security_region_name"]).sum()
    fig = px.bar(df2, y=["Deceased", "Hospital_admission"], barmode="group")

    st.write(fig)