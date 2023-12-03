import streamlit as st
import pandas as pd
from st_files_connection import FilesConnection

conn = st.connection('s3', type=FilesConnection)
df = conn.read('data-streamlit-nicole/recommender_text_v3 - rec_text.csv', input_format='csv', ttl=600)

st.title('Pleasantrees Product Explorer')
# x = st.slider('Select a value')
# st.write(x, 'squared is', x * x)

st.dataframe(df)
n = len(pd.unique(df['product_id']))

col1, col2, col3 = st.columns(spec=3, gap="large")

with col1:  
    st.header("PRODUCTS")

with col2:
    st.header("BRANDS")

with col3:
    st.header("CATEGORIES")


st.metric('Number of Products', n)
m = len(pd.unique(df['brand_name']))
st.metric('Number of Brands', m)
cat = df.category

message = st.chat_message("assistant")
message.write("Hello, human. Would you like my help finding a product?")


add_selectbox = st.sidebar.selectbox(
    'How would you like to find products today?',
    ('Browse by category', 'Browse by brand', 'Ask AI!')
)

if add_selectbox == 'Browse by category':
    st.write(cat)
    
    