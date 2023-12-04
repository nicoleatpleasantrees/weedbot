import streamlit as st
import pandas as pd
from st_files_connection import FilesConnection


st.set_page_config(
    page_title="Pleasantrees Product Explorer",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.image('https://i.postimg.cc/GpxSW0bG/Pleasantrees-logo-sxs-white.png', width=400)

with st.sidebar:
    st.header('Product Explorer')
    st.subheader('Explore our products and find the right one for you!')
    st.caption('Made with ❤️ by Nicole')
