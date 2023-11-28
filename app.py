import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

conn = st.experimental_connection("gsheets",type=GSheetsConnection)
df = conn.read(spreadsheet = "", nrows=25)

st.title('Pleasantrees Product Explorer')
x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

add_selectbox = st.sidebar.selectbox(
    'How would you like to find the perfect product today?',
    ('Browse by category', 'Browse by brand', 'Ask AI!')
)
