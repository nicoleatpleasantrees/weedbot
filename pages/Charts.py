import streamlit as st
import plotly.express as px
from st_files_connection import FilesConnection

st.image('https://i.ibb.co/FJR389Y/Pleasantrees-logo-sxs-white.png', width=400)
st.title('Charts')

conn = st.connection('s3', type=FilesConnection)
df = conn.read('data-streamlit-nicole/strains_for_plotly.csv')

st.subheader("Strains by potency")
st.write("This chart shows the distribution of strains by potency."