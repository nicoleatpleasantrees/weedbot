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

with st.sidebar:
    st.image('https://i.ibb.co/FJR389Y/Pleasantrees-logo-sxs-white.png', width=250)
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

conn = st.connection('s3', type=FilesConnection)
df = conn.read('data-streamlit-nicole/recommender_text_v3 - rec_text.csv', input_format='csv', ttl=600)


st.subheader('Pleasantrees Product Explorer')
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
    message.write("Hello, human. Would you like my help finding a product?")
elif add_selectbox == 'Browse by brand':
    st.write('You selected brand 🎆')
else:
    st.write('You selected category 🥳')
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

# Function for generating LLaMA2 response
def generate_llama2_response(prompt_input):
    string_dialogue = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            string_dialogue += "User: " + dict_message["content"] + "\n\n"
        else:
            string_dialogue += "Assistant: " + dict_message["content"] + "\n\n"
    output = replicate.run(llm, 
                           input={"prompt": f"{string_dialogue} {prompt_input} Assistant: ",
                                  "temperature":temperature, "top_p":top_p, "max_length":max_length, "repetition_penalty":1})
    return output

# User-provided prompt
if prompt := st.chat_input(disabled=not replicate_api):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_llama2_response(prompt)
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)