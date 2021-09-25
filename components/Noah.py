import streamlit as st
import pandas as pd
from utils.constants import API_URL


def riool():
    df_riool = pd.read_csv(API_URL + 'COVID-19_rioolwaterdata.csv', delimiter=';', parse_dates = ["Date_measurement"])
    df_gemeente = df_riool.set_index("RWZI_AWZI_name")

    #laat riool df zien
    riool_cb = st.checkbox('Show Riool dataframe')
    if riool_cb:
        st.write(df_gemeente.sort_index(level=['RWZI_AWZI_name'], ascending=[True]))

    #kies de waarde
    data_switch = st.checkbox("ml aan/uit")
    if data_switch:
        ml = "RNA_per_ml"
    else:
        ml = "RNA_flow_per_100000"

    #stad selectie bar/menu
    stad = st.selectbox('Selecteer een stad om de riooldata te bekijken.',df_riool["RWZI_AWZI_name"].unique())
    data_stad = (df_riool[df_riool["RWZI_AWZI_name"] == stad].set_index("Date_measurement")[ml].sort_index()).dropna()
    st.line_chart(data_stad)

    #bij de stad horende dataframe
    data_stad_cb = st.checkbox('Laat het bijbehorende dataframe zien')
    if data_stad_cb:
        st.write(data_stad)


#st.write(df_gemeente.loc["Assen"])

def ic():
    df_ic = pd.read_csv(API_URL + 'COVID-19_ic_opnames.csv ', delimiter = ';', parse_dates = ["Date_of_statistics"])
    st.line_chart(df_ic.set_index("Date_of_statistics")["IC_admission"])

    #ic_cb = st.checkbox('Show ic dataframe')
    #if ic_cb:
    #    st.write(df_ic)

def testen():
    df_testen = pd.read_csv(API_URL + 'COVID-19_uitgevoerde_testen.csv', delimiter = ';', parse_dates = ["Date_of_statistics"])
    #st.line_chart(df_testen.set_index("Date_of_statistics")["IC_admission"])

    #ic_cb = st.checkbox('Show ic dataframe')
    #if ic_cb:
    #st.write(df_testen)
    regio = st.selectbox('Selecteer een regio om de test data te bekijken.', df_testen["Security_region_name"].unique())
    data_regio = (df_testen[df_testen["Security_region_name"] == regio].set_index("Date_of_statistics").sort_index()).dropna()
    #st.write(data_regio)
    st.line_chart(data_regio["Tested_with_result"])#,data_regio["Tested_positive"])
    st.line_chart(data_regio["Tested_positive"])