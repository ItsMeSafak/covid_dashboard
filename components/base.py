import streamlit as st

def sidebar():
    global showPlots
    global showCode

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


def main():
    sidebar()

