import pandas as pd
import numpy as np
import streamlit as st


logo_path = 'Venturi Dynamics Logo.svg'
st.logo(logo_path,size='large')

col1,col2,col3 = st.columns(3)


col2.image(logo_path,width=200)
st.title('Venturi Dynamics Database',text_alignment="center")
st.markdown("[The location for all the nerdy details for everyone to learn]",text_alignment="center")

st.markdown('''**Welcome** to the database we have built up for our testing and development of our products. 
            Here you'll find everything from comparisons of products compared to ours,
            testing details, and rationale about our decisions. ''')
st.markdown('''
            To navigate the app, use the sidebar to the left and have a look through the different parts of the app. 
            More will come as we continue to develop more products and suits! Further blog posts can be found on our website.
            ''')
col11,col22,col33 = st.columns(3)
col22.link_button('Venturi Dynamics Website','https://www.venturidynamics.com/',help='Open link in new tab')
st.image('Far-tunnel-shot.JPG')
