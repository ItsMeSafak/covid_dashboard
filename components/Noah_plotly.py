import plotly.express as px
import streamlit as st
from utils.helpers import load_data
import components.base as gSlider
import pandas as pd

def testen():
    df_testen = load_data('COVID-19_uitgevoerde_testen.csv',
                            "Date_of_statistics",
                            "Date_of_statistics").sort_index()

    regio = st.selectbox('Selecteer een regio om de test data te bekijken.',
                         sorted(df_testen["Security_region_name"].unique()))

    data_regio = (df_testen[df_testen["Security_region_name"] == regio].dropna())

    start, end = (data_regio.index.min().date(), data_regio.index.max().date())

    # slider
    start_s, end_s = gSlider.start_h, gSlider.end_h #st.slider("Selecteer een periode", start, end, (start, end))
    selected_range_fig = data_regio[start_s:end_s]

    min, max = selected_range_fig.index.min().date(), selected_range_fig.index.max().date()
    periode = str("<br>over periode: " + str(min) + " tot " + str(max))

    # plotly figuur
    fig = px.line(selected_range_fig, x=selected_range_fig.index, y=["Tested_with_result", "Tested_positive"],
                  title="Afgenomen testen met uitslag en positieve uitslagen: " + regio + periode,
                  labels={"Date_of_statistics": 'Datum',
                          "value": "Aantal testen",
                          "variable": "Data",
                          "Tested_with_result": "test"},
                  width=500,
                  height=300)

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
    start_s, end_s = gSlider.start_h, gSlider.end_h #st.slider("Selecteer een periode", start, end, (start, end))
    selected_range_fig = df_ic[start_s:end_s]

    min, max = selected_range_fig.index.min().date(), selected_range_fig.index.max().date()
    periode = str("<br>over periode: " + str(min) + " tot " + str(max))

    # plotly figuur
    fig = px.line(selected_range_fig, x=selected_range_fig.index, y="IC_admission",
                  title="Landelijke IC Opnames" + periode,
                  labels={"Date_of_statistics": 'Datum',
                          "IC_admission": "Aantal IC Opnames"},
                width=500,
                height=300)
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
        ml = ("RNA_flow_per_100000", "RNA flow per 100000 inwoners")

    # stad selectie dataframe
    data_stad = df_riool[df_riool["RWZI_AWZI_name"] == rwzi][ml[0]].dropna().sort_index()
    if not(data_stad.empty or len(data_stad) <= 2):
        # slider periode
        start, end = (data_stad.index.min().date(), data_stad.index.max().date())
        start_s, end_s = gSlider.start_h, gSlider.end_h #st.slider("Selecteer een periode", start, end, (start, end))

        # slice dataframe
        selected_range_fig = data_stad[start_s:end_s]
        min, max = selected_range_fig.index.min().date(), selected_range_fig.index.max().date()
        periode = str("<br>over periode: " + str(min) + " tot " + str(max))

        # plotly
        fig = px.line(selected_range_fig, x=selected_range_fig.index, y=ml[0],
                      title="Rioolwater data: " + rwzi + periode,
                      labels={'Date_measurement': 'Datum',
                              ml[0]: ml[1]}, markers="o",
                      width=500,
                      height=300)
        st.write(fig)
    else:
        st.write("Data ontbreekt voor selectie, deze data is aanwezig:")
        st.write(data_stad)


def Opname_overlijden():
    df = load_data('COVID-19_aantallen_gemeente_per_dag.csv',
                            "Date_of_publication",
                            "Date_of_publication").dropna()

    # nog een catch nodig in geval van lege lijst
    region = st.multiselect('Selecteer een regio om de test data te bekijken.',
                            sorted(df["Security_region_name"].unique()),
                            default=sorted(df["Security_region_name"].unique()))


                            default=sorted(df["Security_region_name"].unique())[0:3] )
    if not(region == []):
        df2 = df.loc[df["Security_region_name"].isin(region)]
        start, end = (df2.index.min().date(), df2.index.max().date())
        # slider
        start_s, end_s = gSlider.start_h, gSlider.end_h#st.slider("Selecteer een periode", start, end, (start, end))

        df2 = df2[start_s:end_s]

        min, max = df2.index.min().date(), df2.index.max().date()
        periode = str("<br>over periode: " + str(min) + " tot " + str(max))

        df2 = df2.groupby(["Security_region_name"]).sum()
        fig = px.bar(df2, y=["Deceased", "Hospital_admission"], barmode="group", title ="Ziekenhuis opnames en dodental per Regio" + periode, width=500, height=300)
        st.write(fig)


def sex_dec():

    df = load_data('COVID-19_casus_landelijk.csv',
                            "Date_statistics",
                            "Date_statistics")

    start_s, end_s = gSlider.start_h, gSlider.end_h
    df = df[start_s:end_s]
    df = df.reset_index()

    df4 = pd.get_dummies(df["Deceased"])

    df4 = pd.concat([df, df4], axis=1)
    df5 = df4.groupby("Sex").sum() #.drop("Unknown")

    min, max = df["Date_statistics"].min().date(), df["Date_statistics"].max().date()
    periode = str("<br>over periode: " + str(min) + " tot " + str(max))

    fig = px.bar(df5, y=["Yes", "No", "Unknown"], title= "mensen met covid/dodental"+ periode)
    st.write(fig)
