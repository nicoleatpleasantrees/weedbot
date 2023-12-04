import streamlit as st
import pandas as pd
from hugchat import hugchat
from hugchat.login import Login

st.image('https://i.postimg.cc/GpxSW0bG/Pleasantrees-logo-sxs-white.png', width=400)
st.subheader('Weedbot')

with st.sidebar:
    st.subheader("Enter your Hugging Face credentials")
    if ("EMAIL" in st.secrets) and ("PASSWORD" in st.secrets): 
            st.success("Credentials already provided.")
            hf_email = st.secrets["EMAIL"]
            hf_password = st.secrets["PASSWORD"]
    else:
          hf_email = st.text_input("Enter email address:", type="password")
          hf_password = st.text_input("Enter password:", type="password")
          if not (hf_email and hf_password):
              st.warning("Please enter your credentials!", icon="⚠️")
          else:
              st.success('Login successful! You may now proceed to the weed...')       
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "What questions do you have for the Weedbot🔮?"}]
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

def generate_response(prompt_input, email, passwd):
    # Hugging Face Login
    sign = Login(email, passwd)
    cookies = sign.login()
    # Create ChatBot                        
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbot.chat(prompt_input)

if prompt := st.chat_input(disabled=not (hf_email and hf_password)):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_response(prompt, hf_email, hf_password) 
            st.write(response) 
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)        


