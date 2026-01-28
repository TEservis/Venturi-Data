import pandas as pd
import numpy as np
import streamlit as st



#st.set_page_config(layout=("centered"))
    
pages = {
    
    "Navigation":[
        st.Page('pages/home_page.py',title='Home'),
    ],
    "Testing": [
        st.Page("pages/rho_test_report.py", title="Rho Testing Report: 10 Jan 2026")
    ],
}
    
pg = st.navigation(pages,position="sidebar")
pg.run()

st.sidebar.page_link('https://www.venturidynamics.com/shop',label='**Shop**')
