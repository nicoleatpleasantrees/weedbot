import streamlit as st
import pandas as pd
from st_files_connection import FilesConnection
from hugchat import hugchat
from hugchat.login import Login

st.set_page_config(
    page_title="Pleasantrees Product Explorer",
    page_icon="🌿",
)

conn = st.connection('s3', type=FilesConnection)
df = conn.read('data-streamlit-nicole/strain_match_product.csv')

st.image('https://i.postimg.cc/GpxSW0bG/Pleasantrees-logo-sxs-white.png', width=400)

with st.sidebar:
    st.header('Product Explorer')
    st.subheader('Explore our products and find the right one for you!')
    option = st.selectbox('How would you like to shop?', ['Ask Weedbot', 'By Category', 'By Brand', 'By Strain', 'By Price Range', 'By Potency Range'])