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
df = conn.read('data-streamlit-nicole/strains_for_plotly.csv')
df2 = conn.read('data-streamlit-nicole/strain_match_product.csv')

st.image('https://i.postimg.cc/GpxSW0bG/Pleasantrees-logo-sxs-white.png', width=400)

minimum_thc = df['average THC'].min()
maximum_thc = df['average THC'].max()
minimun_price = df2['price'].min()
maximum_price = df2['price'].max()
categories = df2.category.values.tolist()
brands = df2.brand.values.tolist()
strains = df2.strain.values.tolist()

with st.sidebar:
    st.header('Product Explorer')
    st.subheader('Explore our products and find the right one for you!')
    option = st.selectbox('How would you like to shop?', ['Ask Weedbot', 'By Category', 'By Brand', 'By Strain', 'By Price Range', 'By Potency Range'])
