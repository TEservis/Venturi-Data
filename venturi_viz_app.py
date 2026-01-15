import pandas as pd
import numpy as np
import streamlit as st



st.set_page_config(layout=("centered"))



st.header('Data from suit test 10th of Jan 2026',text_alignment='center')
st.markdown('[Location: Silverstone Sports Engineering Hub]',text_alignment='center') 


col1,col2 = st.columns(2)
col1.markdown('''This was our initial test for the new Venturi Rho Triathlon Suit to 
            gather data to see how it performed against other suits of the same caliber, i.e. high temperature triathlon suits. ''')


col1.markdown('''The Venturi Rho Triathlon suit were developed specifically to perform for the masses and not just the pros. 
                Great thermal regulation due to the colour and chosen fabrics as well as a great chamois for long events 
                (from testing both in racing and long hours on the turbo).''')

col1.markdown('''The other suits tested were a Team GB triathlon suit, Nopinz Flow Subzero, and the Rapha Men's Pro Team Summer Roadsuit.''')

col2.image('Bepton.png')

st.markdown('''The main difference between the three other suits that were tested is the price, where something like the Rapha suit goes for 
            at least the double of the Venturi Rho, which means >> £300 as well as the speed rating of which the suit performs best in.''')
st.markdown(''' 
            For example, the Rapha Roadsuit is designed for world tour stage victories reaching up to speeds of 50 kp/h
            and it is visible in the data below that for the lower speeds, it performs worse. This means that for
            someone that doesn't race at these speeds, you are better of with something like the Rho suit that we have developed.''')

from venturi_test_data_10jan26 import fig_yaw
st.pyplot(fig_yaw)
st.caption("Test data for various yaw angles. For each yaw angle, each suit's CdA is displayed varying over the speeds tested at")
