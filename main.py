import streamlit

import components.cool_plot as cool_plot
import components.File_01 as File_01
import components.Noah as Noah

# Test comment 7
if __name__ == "__main__":
    cool_plot.main()
    File_01.main()

    noah_on = streamlit.checkbox("Noah probeersels")
    if noah_on:
        riool_on = streamlit.checkbox("Riool")
        if riool_on: Noah.riool()
        ic_on = streamlit.checkbox("IC opnames")
        if ic_on: Noah.ic()
