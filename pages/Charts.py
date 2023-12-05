import streamlit as st
import plotly.express as px
from st_files_connection import FilesConnection

st.image('https://i.ibb.co/FJR389Y/Pleasantrees-logo-sxs-white.png', width=400)
st.title('Charts')

conn = st.connection('s3', type=FilesConnection)
df = conn.read('data-streamlit-nicole/strains_for_plotly.csv')

st.subheader("Strains by potency")

fig = px.histogram(
    data_frame=df, x=df["average THC"],
    color=df["type"], marginal="rug",
    nbins=8,
    hover_data=df.columns
    )
st.plotly_chart(fig, use_container_width=False,sharing='streamlit', theme='streamlit')