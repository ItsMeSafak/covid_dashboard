import streamlit as st
from datetime import date




def sidebar():
    global showPlots
    global showCode
    global start_h
    global end_h
    global showBackground

    # Initial page config
    st.set_page_config(
        page_title='COVID-19 Dashboard',
        layout='wide',
        initial_sidebar_state="expanded"
    )

    st.sidebar.header('Dashboard setings')
    st.sidebar.write('Display settings:')

    showPlots = st.sidebar.checkbox('Show plots', True)
    showCode = st.sidebar.checkbox('Show code', False)
    showBackground = st.sidebar.checkbox('Achtergrond afbeelding', True)

    #datum selector
    start_h, end_h = (date(2020, 8, 1), date.today())
    st.sidebar.write("Selecteer een start en eind datum:")
    start_h = st.sidebar.date_input('Start datum', start_h, key = "startd")
    end_h = st.sidebar.date_input('Eind datum', end_h, key = "endd")

    start_h, end_h = st.sidebar.slider("Selecteer een periode", start_h, end_h,
                                       (start_h, end_h), key="Globalslider")


# mischien leuk met bg img, als het mogelijk is moet de achtergrondstijd van de widgets nog aangepast worden (rounded corners ofz)
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


