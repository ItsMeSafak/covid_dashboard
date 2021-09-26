import streamlit as st
import inspect

import components.Noah_plotly as figg
import components.base as base

def show_with_options(header, func):
    st.header(header)
    if base.showPlots: func()
    if base.showCode: st.code(inspect.getsource(func))

def initialize_plots():
    show_with_options('Landelijke IC opnames', figg.ic)
    show_with_options('Afgenomen tests', figg.testen)
    show_with_options('Rioolwater data', figg.riool)

if __name__ == "__main__":
    base.main()
    initialize_plots()

    
