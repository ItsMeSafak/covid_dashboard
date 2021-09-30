import streamlit as st
from datetime import date

def sidebar():
    # Global variables to check on plots
    global showPlots
    global showCode
    global start_h
    global end_h
    global showBackground
    global region

    # Initial page config
    st.set_page_config(
        page_title='COVID-19 Dashboard',
        layout='wide',
        initial_sidebar_state="expanded"
    )

    st.sidebar.header('Dashboard setings')
    st.sidebar.write('Display settings:')

    # Checkboxes for showing plots/code
    showPlots = st.sidebar.checkbox('Show plots', True)
    showCode = st.sidebar.checkbox('Show code', False)
    showBackground = st.sidebar.checkbox('Achtergrond afbeelding', True)

    # Date selector
    start_h, end_h = (date(2020, 8, 1), date.today())
    st.sidebar.header("Selecteer een start en eind datum:")
    start_h = st.sidebar.date_input('Start datum', start_h, key = "startd")
    end_h = st.sidebar.date_input('Eind datum', end_h, key = "endd")

    # Slider for date
    start_h, end_h = st.sidebar.slider("Selecteer een periode", start_h, end_h,
                                       (start_h, end_h), key="Globalslider")

    # Multi select for regions
    st.sidebar.markdown('*Deze multi select is alleen van toepassing op sectie 2*')
    region = st.sidebar.multiselect('Selecteer een regio om de data te bekijken.',
                            sorted(['Groningen', 'Flevoland', 'Fryslân', 'Drenthe', 'Twente', 'IJsselland',
                                            'Noord- en Oost-Gelderland', 'Gelderland-Midden', 'Gelderland-Zuid',
                                            'Utrecht', 'Amsterdam-Amstelland', 'Noord-Holland-Noord',
                                            'Zaanstreek-Waterland', 'Kennemerland', 'Gooi en Vechtstreek',
                                            'Zuid-Holland-Zuid', 'Hollands-Midden', 'Rotterdam-Rijnmond', 'Haaglanden',
                                            'Zeeland', 'Brabant-Zuidoost', 'Midden- en West-Brabant', 'Brabant-Noord',
                                            'Limburg-Zuid', 'Limburg-Noord']),
                                    default= sorted(['Groningen', 'Flevoland', 'Fryslân', 'Drenthe', 'Twente', 'IJsselland',
                                            'Noord- en Oost-Gelderland', 'Gelderland-Midden', 'Gelderland-Zuid',
                                            'Utrecht', 'Amsterdam-Amstelland', 'Noord-Holland-Noord',
                                            'Zaanstreek-Waterland', 'Kennemerland', 'Gooi en Vechtstreek',
                                            'Zuid-Holland-Zuid', 'Hollands-Midden', 'Rotterdam-Rijnmond', 'Haaglanden',
                                            'Zeeland', 'Brabant-Zuidoost', 'Midden- en West-Brabant', 'Brabant-Noord',
                                            'Limburg-Zuid', 'Limburg-Noord']))
    st.sidebar.markdown('*Documentation: https://github.com/ItsMeSafak/covid_dashboard/blob/master/README.md*')

def set_bg():
    if showBackground:
        st.markdown(
            """
             <style>
            .reportview-container {
               background: url("https://static.vecteezy.com/system/resources/previews/000/697/526/non_2x/virus-pattern-on-a-dark-background-vector.jpg")
            }
            </style>
            """,
            unsafe_allow_html=True
         )

def main():
    sidebar()
    set_bg()
