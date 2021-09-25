import streamlit

import components.cool_plot as cool_plot
import components.File_01 as File_01
import components.Noah as Noah
import components.Noah_plotly as figg
# Test comment 7
if __name__ == "__main__":
    cool_plot.main()
    File_01.main()

    noah_on = streamlit.checkbox("Noah probeersels")
    if noah_on:

        ic_on = streamlit.checkbox("Landelijke IC opnames")
        if ic_on: figg.ic()

        riool_on = streamlit.checkbox("Rioolwater Data per rioolwaterzuiveringsinstalatie")
        if riool_on: figg.riool()

        testen_on = streamlit.checkbox("Afgenomen Testen per regio")
        if testen_on: figg.testen()
