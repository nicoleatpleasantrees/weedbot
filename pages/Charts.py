import streamlit as st
import plotly.express as px
from st_files_connection import FilesConnection

st.image('https://i.ibb.co/FJR389Y/Pleasantrees-logo-sxs-white.png', width=400)

conn = st.connection('s3', type=FilesConnection)
df = conn.read('data-streamlit-nicole/strains_for_plotly.csv')


st.subheader("Strains by potency")
st.markdown("This chart shows the distribution of strains by potency range.")

fig = px.histogram(
    data_frame=df, x=df["average THC"],
    color=df["type"], marginal="rug",
    nbins=8,
    hover_data=df.columns
    )
st.plotly_chart(fig, use_container_width=False,sharing='streamlit', theme='streamlit')

st.subheader("Strains by type")

fig_2 = px.treemap(
    data_frame=df, path=[px.Constant("all"), "type", "strain"],
    values="average THC",
    color="average THC",
    color_continuous_scale="RdBu",
    hover_data=["average THC"],
    )

st.plotly_chart(fig_2, use_container_width=True,sharing='streamlit', theme='streamlit')
