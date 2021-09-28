import streamlit as st
import inspect
#test
import components.Noah_plotly as noh_figg
import components.sfk_plots as sfk_figg

import components.base as base

def show_with_options(header, func):
    st.header(header)
    if base.showPlots: func()
    if base.showCode: st.code(inspect.getsource(func))

def initialize_plots():
    col1, col2, col3 = st.columns([4, 1, 4])

    with col1:
        show_with_options('Landelijke IC opnames', noh_figg.ic)
        show_with_options('Afgenomen testen', noh_figg.testen)
        show_with_options('Leeftijds groepen', sfk_figg.age_groups)

    with col3:
        show_with_options('Rioolwater data', noh_figg.riool)
        show_with_options('Ziekenhuis opnames en dodental', noh_figg.Opname_overlijden)

if __name__ == "__main__":
    base.main()
    initialize_plots()

    
