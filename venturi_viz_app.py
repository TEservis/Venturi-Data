import pandas as pd
import numpy as np
import streamlit as st

from venturi_test_data_10jan26 import fig_yaw
from venturi_test_data_10jan26 import figg


st.set_page_config(layout=("centered"))



st.header('Data from suit test 10th of Jan 2026',text_alignment='center')
st.markdown('[Location: Silverstone Sports Engineering Hub]',text_alignment='center') 


col1,col2 = st.columns(2)
col1.markdown('''This was our initial test for the new Venturi RHO Triathlon Suit to 
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
            someone that doesn't race at these speeds, you are better of with something like the RHO suit that we have developed.''')


st.pyplot(fig_yaw)
st.caption("Test data for various yaw angles. For each yaw angle, each suit's CdA is displayed varying over the speeds tested at")

st.subheader('Testing Protocol')
st.markdown('''Four suits were tested as stated above. Each at 0°,5°,10°,and 15° yaw. For each yaw angle,
                the suits were tested at 30,35,and 45 kp/h within the accuracy of the SSEH Sports Performance Wind Tunnel.
                For each test event (example: 35 kp/h @ 10° yaw) the data was averaged over 30 seconds to capture the effects caused by
                the pedalling motion of the legs. 
            ''')
st.markdown('''Every test run was calibrated beforehand across all yaw angles, and between the change in yaw and recording data,
            the airflow was allowed to stabilise for 5 seconds before recording started.
            Due to a client testing session taking 3hrs beforehand, the air was well circulated in the tunnel.
            ''')

st.pyplot(figg)
st.caption('''This chart displays the difference in watts for each of the speeds, assuming an air density of 1.225kg/m^3 and
           is calculated for each velocity displayed. The watts displayed are calculated by W_suit - W_VenturiRHO at each speed.
           ''')

st.markdown('''
            Based on the above the RHO is performing very well, proving faster than almost all suits at all yaw angles and speeds. 
            ''')
st.markdown('''
            But the most important part is the performance at higher yaw angles. If you imagine a race, you will most likely face
            cross wind and such which will cause an effective wind direction acting on you.
            ''')
st.markdown('''
            At lower speeds, yaw angles are more prominent due to that the nominal velocity vector is smaller than at higher speeds. 
            Therefore, at lower speeds, for a weaker cross wind, you will experience higher yaw angles as compared to someone 
            riding at higher speeds.
            ''')
st.markdown('''
            Given that the RHO is performing excellent at higher yaw angles, outperforming all the suits at all speeds, 
            **this is the suit for you**
            ''')
