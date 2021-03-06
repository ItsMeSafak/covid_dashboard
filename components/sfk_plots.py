import streamlit as st
import plotly.express as px
import components.base as gSlider
from utils.helpers import load_data


def admissions_plot():
    df_opnames_age = load_data('COVID-19_ziekenhuis_ic_opnames_per_leeftijdsgroep.csv', dates="Date_of_statistics_week_start", index="Date_of_statistics_week_start")
    df_opnames_dropped = df_opnames_age.drop(columns=['Version', 'Date_of_report'])

    # Slice dataframe with global date slider
    df_opnames_dropped = df_opnames_dropped[gSlider.start_h: gSlider.end_h]
    min, max = df_opnames_dropped.index.min().date(), df_opnames_dropped.index.max().date()
    periode = str("<br>over periode: " + str(min) + " tot " + str(max))

    # Reset to make sure nothing else is changed
    df_opnames_dropped = df_opnames_dropped.reset_index()
    df_grouped_by_age = df_opnames_dropped.groupby('Age_group').sum()

    region = st.multiselect('Selecteer een leeftijdsgroep om de data te bekijken.',
                            sorted(df_grouped_by_age.index),
                            default=sorted(df_grouped_by_age.index[0:2]))
    fig2 = px.line(df_opnames_dropped[df_opnames_dropped['Age_group'].isin(region)], x='Date_of_statistics_week_start', y="Hospital_admission", color='Age_group', labels={
        "Hospital_admission": "Ziekenhuis opnames",
        "Date_of_statistics_week_start": "Datum van statistiek opname",
        "Age_group": "Leeftijdsgroep"
    }, width=500, height=400, title="Ziekenhuis opnames over verloop van tijd<br>per leeftijdsgroep" + periode)

    st.plotly_chart(fig2, use_container_width=True)

def age_groups_plot():
    df_opnames_age = load_data('COVID-19_ziekenhuis_ic_opnames_per_leeftijdsgroep.csv', dates="Date_of_statistics_week_start", index="Date_of_statistics_week_start")
    df_opnames_dropped = df_opnames_age.drop(columns=['Version', 'Date_of_report'])

    # Slice dataframe with global date slider
    df_opnames_dropped = df_opnames_dropped[gSlider.start_h: gSlider.end_h]
    min, max = df_opnames_dropped.index.min().date(), df_opnames_dropped.index.max().date()
    periode = str("<br>over periode: " + str(min) + " tot " + str(max))

    # reset to make sure nothing else is changed
    df_opnames_dropped = df_opnames_dropped.reset_index()

    df_grouped_by_age = df_opnames_dropped.groupby('Age_group').sum()
    fig = px.bar(df_grouped_by_age, y=["Hospital_admission", "IC_admission"], barmode="group", labels={
        "value": "Aantal mensen",
        "Age_group": "Leeftijdsgroepen",
        "variable": "Legenda",
    }, width=500, height=400, title="Landelijke opnames per leeftijdsgroep" + periode)
    fig.data[0].name = "Ziekenhuisopnames"
    fig.data[1].name = "IC Opnames"
    st.plotly_chart(fig, use_container_width=True)

   
