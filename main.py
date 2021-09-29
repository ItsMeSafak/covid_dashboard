import streamlit as st
import inspect

import components.Noah_plotly as noh_figg
import components.sfk_plots as sfk_figg
import components.Fleur as fleur
import components.base as base

def show_with_options(header, func):
    st.header(header)
    if base.showPlots: func()
    if base.showCode: st.code(inspect.getsource(func))

def initialize_plots():
    st.markdown(
            """
             <style>
            div[data-testid="stHorizontalBlock"] {
                background-color: rgba(20, 20, 20, .8);
                border-radius: 10px;
                padding: 20px;
                margin-bottom: 50px;   
            }

            #covid-19-dashboard {
                background-color: rgba(20, 20, 20, .8);
                border-radius: 10px;
                padding: 20px;
                margin-bottom: 50px;  
            }

            </style>
            """,
            unsafe_allow_html=True
         )
        
    st.header('COVID-19 Dashboard')

    _, header_col, _ = st.columns([1, 8, 1])
    col1, _, col3 = st.columns([4, 1, 4])
    col4, _, col6 = st.columns([4, 1, 4])
    col7, _, col9 = st.columns([4, 1, 4])

    with header_col:
        show_with_options('Landelijke IC opnames', noh_figg.ic)

    with col1:
        st.markdown('*Sectie 1*')
        show_with_options('Dodental per geslacht', noh_figg.sex_dec)

    with col3:
        st.markdown('  ')
        st.markdown('  ')
        show_with_options('Reproductie getal', fleur.reproG)
        show_with_options('Leeftijdsgroepen', sfk_figg.age_groups)
    
    with col4:
        st.markdown('*Sectie 2*')
        show_with_options('Afgenomen testen', noh_figg.testen2)
    with col6:
        st.markdown(' ')
        show_with_options('Ziekenhuisopnames en dodental', noh_figg.Opname_overlijden2)

    with col7:
        st.markdown('*Sectie 3*')
        show_with_options('Ziekenhuisopnames in leeftijdsgroepen', sfk_figg.admissions)
    with col9:
        st.write('  ')
        show_with_options('Rioolwater data', noh_figg.riool)


if __name__ == "__main__":
    base.main()
    initialize_plots()

    
