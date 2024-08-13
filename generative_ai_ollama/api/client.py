import requests
import streamlit as st


def get_fakeai_response(input_text):
    response = requests.post('http://localhost:8085/song/invoke',
                             json={'input': {'topic': input_text}})

    return response.json()['output']


def get_ollama_response(input_text):
    response = requests.post('http://localhost:8085/topten/invoke',
                             json={'input': {'topic': input_text}})

    return response.json()['output']

# streamlit framework


st.title('Langchain demo with fakeAPI and Ollama API')
user_text = st.text_input('Write a song on')
user_text1 = st.text_input('Write a song for the ollama llm')

if user_text:
    st.write(get_fakeai_response(user_text))

if user_text1:
    st.write(get_ollama_response(user_text1))