import requests
import streamlit as st 

def get_ollama_response(input_text):
    response=requests.post("http://localhost:8000/essay/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']

def get_ollama_response2(input_text):
    response=requests.post("http://localhost:8000/poem/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']


## streamlit framework

st.title('Essay & Poem Writer by Etu')
input_text=st.text_input("Write an Essay on")
input_text1=st.text_input("Write a Poem on")

if input_text:
    st.write(get_ollama_response(input_text))

if input_text1:
    st.write(get_ollama_response2(input_text1))
