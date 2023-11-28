import streamlit as st
import pandas as pd

st.title('Pleasantrees Product Explorer')

st.connections.SnowflakeConnection('pmb32940.us-east-1.snowflakecomputing.com')

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

add_selectbox = st.sidebar.selectbox(
    'How would you like to find the perfect product today?',
    ('Browse by category', 'Browse by brand', 'Ask AI!')
)