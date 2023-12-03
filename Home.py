import streamlit as st
import pandas as pd
import replicate
from st_files_connection import FilesConnection

st.set_page_config(
    page_title="Pleasantrees Product Explorer",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.image('https://i.ibb.co/FJR389Y/Pleasantrees-logo-sxs-white.png', width=400)

with st.sidebar:
    st.header('Product Explorer')
    st.subheader('Explore our products and find the right one for you!')
    st.caption('Made with ❤️ by Nicole')
   
    if 'REPLICATE_API_TOKEN' in st.secrets:
        st.success('API key already provided!', icon='✅')
        replicate_api = st.secrets['REPLICATE_API_TOKEN']
    else:
        replicate_api = st.text_input('Enter Replicate API token:', type='password')
        if not (replicate_api.startswith('r8_') and len(replicate_api)==40):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')
        st.subheader('Models and parameters')
    selected_model = st.sidebar.selectbox('Choose a Llama2 model', ['Llama2-7B', 'Llama2-13B', 'Llama2-70B'], key='selected_model')
    if selected_model == 'Llama2-7B':
        llm = 'a16z-infra/llama7b-v2-chat:4f0a4744c7295c024a1de15e1a63c880d3da035fa1f49bfd344fe076074c8eea'
    elif selected_model == 'Llama2-13B':
        llm = 'a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5'
    else:
        llm = 'replicate/llama70b-v2-chat:e951f18578850b652510200860fc4ea62b3b16fac280f83ff32282f87bbd2e48'        

    temperature = st.sidebar.slider('temperature', min_value=0.01, max_value=5.0, value=0.1, step=0.01)
    top_p = st.sidebar.slider('top_p', min_value=0.01, max_value=1.0, value=0.9, step=0.01)
    max_length = st.sidebar.slider('max_length', min_

conn = st.connection('s3', type=FilesConnection)
df = conn.read('data-streamlit-nicole/recommender_text_v3 - rec_text.csv', input_format='csv', ttl=600)

st.image('https://i.ibb.co/FJR389Y/Pleasantrees-logo-sxs-white.png', width=400)
st.header('Cannabis Experience Optimization Engine')
st.text('But you can call me Weedbot')
# st.dataframe(df)
n = len(pd.unique(df['product_id']))
st.metric('Number of Products', n)
m = len(pd.unique(df['brand_name']))
st.metric('Number of Brands', m)
cat = df.category

add_selectbox = st.sidebar.selectbox(
    'How would you like to shop?',
    ('Browse by category', 'Browse by brand', 'Ask AI!')
)

if add_selectbox == 'Ask AI!':
    message = st.chat_message("assistant")
    message.write("Hello, human. You can call me Weedbot. Would you like my help finding a product?")
elif add_selectbox == 'Browse by brand':
    st.write('You selected brand 🎆')
else:
    st.write('You selected category 🥳')
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

