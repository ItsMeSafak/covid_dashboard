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
    col1, _, col3 = st.columns([4, 1, 4])
    st.markdown(
            """
             <style>
            div[data-testid="stHorizontalBlock"] {
                background-color: rgba(20, 20, 20, .8);
                border-radius: 10px;
                padding: 20px;
            }
            </style>
            """,
            unsafe_allow_html=True
         )

    with col1:
        show_with_options('Landelijke IC opnames', noh_figg.ic)
        show_with_options('Afgenomen testen', noh_figg.testen2)
        show_with_options('Leeftijds groepen', sfk_figg.age_groups)

    with col3:
        show_with_options('Rioolwater data', noh_figg.riool)
        show_with_options('Ziekenhuis opnames en dodental', noh_figg.Opname_overlijden2)
        show_with_options('dodental', noh_figg.sex_dec)
        show_with_options('Reproductie getal', fleur.reproG)

if __name__ == "__main__":
    base.main()
    initialize_plots()

    
