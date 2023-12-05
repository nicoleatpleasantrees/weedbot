import streamlit as st
import pandas as pd
from st_files_connection import FilesConnection
from hugchat import hugchat
from hugchat.login import Login

st.set_page_config(
    page_title="Pleasantrees Product Explorer",
    page_icon="🌿",
)

st.image('https://i.postimg.cc/GpxSW0bG/Pleasantrees-logo-sxs-white.png', width=400)

with st.sidebar:
    st.header('Product Explorer')
    st.subheader('Explore our products and find the right one for you!')
    st.selectbox('Select a product category', ['Flower', 'Vape', 'Edible', 'Concentrate', 'Topical', 'Accessory'])
    st.caption('Made with ❤️ by Nicole')

    