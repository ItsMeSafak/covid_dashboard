import components.base as gSlider
import pandas as pd
import plotly.express as px
import streamlit as st
from utils.helpers import load_data


def ic_plot():
    df_ic = load_data('COVID-19_ic_opnames.csv',
                            "Date_of_statistics",
                            "Date_of_statistics").sort_index()

    # Slider component
    start_s, end_s = gSlider.start_h, gSlider.end_h
    selected_range_fig = df_ic[start_s:end_s]

    min, max = selected_range_fig.index.min().date(), selected_range_fig.index.max().date()
    periode = str("<br>over periode: " + str(min) + " tot " + str(max))

    # Instantiation of line plot
    fig = px.line(selected_range_fig, x=selected_range_fig.index, y="IC_admission",
                  title="Landelijke IC Opnames" + periode,
                  labels={"Date_of_statistics": 'Datum',
                          "IC_admission": "Aantal IC Opnames"},
                width=500,
                height=400)
    st.plotly_chart(fig, use_container_width=True)

def sewer_plot():
    df_riool = load_data('COVID-19_rioolwaterdata.csv',
                            "Date_measurement",
                            "Date_measurement").sort_index()

    # Select region
    rwzi = st.selectbox('Selecteer een stad om de riooldata te bekijken.',
                        sorted(df_riool["RWZI_AWZI_name"].unique()),
                        index= sorted(df_riool["RWZI_AWZI_name"].unique()).index("Amsterdam West"))

    # City selection
    data_stad = df_riool[df_riool["RWZI_AWZI_name"] == rwzi]["RNA_flow_per_100000"].dropna().sort_index()
    if not(data_stad.empty or len(data_stad) <= 2):

        # Slider period
        start_s, end_s = gSlider.start_h, gSlider.end_h 

        # Slicing of the dataframe
        selected_range_fig = data_stad[start_s:end_s]
        min, max = selected_range_fig.index.min().date(), selected_range_fig.index.max().date()
        periode = str("<br>over periode: " + str(min) + " tot " + str(max))

        # Instantiation of line port
        fig = px.line(selected_range_fig, x=selected_range_fig.index, y="RNA_flow_per_100000",
                      title="Rioolwater data: " + rwzi + periode,
                      labels={'Date_measurement': 'Datum',
                              "RNA_flow_per_100000": "RNA flow per 100000 inwoners"}, markers="o",
                      width=500,
                      height=400)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("Data ontbreekt voor selectie, deze data is aanwezig:")
        st.write(data_stad)

def sex_dec_plot():
    pre_title = ''
    df = load_data('COVID-19_casus_landelijk.csv',
                            "Date_statistics",
                            "Date_statistics")

    start_s, end_s = gSlider.start_h, gSlider.end_h
    df = df[start_s:end_s]
    df = df.reset_index()

    df4 = pd.get_dummies(df["Deceased"])
    df4 = pd.concat([df, df4], axis=1)
    df5 = df4.groupby("Sex").sum()

    min, max = df["Date_statistics"].min().date(), df["Date_statistics"].max().date()
    periode = str("<br>over periode: " + str(min) + " tot " + str(max))

    fig = px.bar(df5, y=["Yes", "No", "Unknown"], labels={
        "value": "Aantal mensen",
        "x": "Geslacht",
        "variable": "Legenda",
    }, x=["Vrouwen", "Mannen"], title= "Mensen met covid/dodental"+ periode, width=500, height=400)
    fig.data[0].name = "Overleden"
    fig.data[1].name = "Overleefd"
    fig.data[2].name = "Onbekend"
    st.plotly_chart(fig, use_container_width=True)

    header = st.header('Verdeling overleden')
    show_death = st.checkbox('Overleefd', False, key="death")

    if show_death:
        var = "No"
        pre_title = "Overleefd"
        df6 = df4.groupby("Agegroup").sum()
        ind = df6.index
        header.header('Verdeling overleefd')
    else:
        var = "Yes"
        pre_title = "Overleden"
        df6 = df4.groupby("Agegroup").sum()[5:]
        ind = df4.groupby("Agegroup").sum().index[5:]
        header.header('Verdeling overleden')

    fig = px.pie(df6, values=var, names=ind, title= pre_title +'/Leeftijdsgroep' + periode, width=500, height=400)
    st.plotly_chart(fig, use_container_width=True)

def death_admission_plot():
    df = load_data('COVID-19_aantallen_gemeente_per_dag.csv',
                            "Date_of_publication",
                            "Date_of_publication").dropna()

    if not(gSlider.region == []):
        start_s, end_s = gSlider.start_h, gSlider.end_h
        df2 = df.loc[df["Security_region_name"].isin(gSlider.region)][start_s:end_s]

        min, max = df2.index.min().date(), df2.index.max().date()
        periode = str("<br>over periode: " + str(min) + " tot " + str(max))

        df2 = df2.groupby(["Security_region_name"]).sum()
        fig = px.bar(df2, y=["Deceased", "Hospital_admission"], barmode="group",
        labels={
            "value": "Aantal mensen",
            "Security_region_name": "Veiligheidsregio's",
            "variable": "Legenda"
        }, title ="Ziekenhuisopnames en dodental per Regio" + periode, width=500, height=400)
        fig.data[0].name = "Overleden"
        fig.data[1].name = "Ziekenhuisopnames"
        st.plotly_chart(fig, use_container_width=True)

def tests_plot():
    st.write('  ')
    df_testen = load_data('COVID-19_uitgevoerde_testen.csv',
                            "Date_of_statistics",
                            "Date_of_statistics").sort_index()

    if not(gSlider.region == []):
         start_s, end_s = gSlider.start_h, gSlider.end_h
         selected_range_fig = df_testen.loc[df_testen["Security_region_name"].isin(gSlider.region)][start_s:end_s]

         min, max = selected_range_fig.index.min().date(), selected_range_fig.index.max().date()
         periode = str("<br>over periode: " + str(min) + " tot " + str(max))
         selected_range_fig = selected_range_fig.groupby("Date_of_statistics").sum()

         # Instantiation of line plot
         fig = px.line(selected_range_fig, x=selected_range_fig.index, y=["Tested_with_result", "Tested_positive"],
                      title="Afgenomen testen met uitslag en positieve uitslagen<br>voor geselecteerde veiligheidsregio's: " +  periode,
                      labels={"Date_of_statistics": 'Datum',
                              "value": "Aantal testen",
                              "variable": "Data",
                              "Tested_with_result": "test"},
                      width=500,
                      height=400)

         fig.data[0].name = "Afgenomen testen <br> met uitslag"
         fig.data[1].name = "Afgenomen testen <br> met positief resultaat"
         st.plotly_chart(fig, use_container_width=True)