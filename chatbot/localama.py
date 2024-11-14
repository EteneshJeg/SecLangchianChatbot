from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM


import streamlit as st 
import os
from dotenv import load_dotenv

load_dotenv()


#langsmith tracking
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# Prompt Template
prompt = ChatPromptTemplate.from_template(
    template="You are a helpful assistant. Please respond to the user's queries. Question: {question}"
)


# Streamlit framework

st.title('Langchain Demo with LLAMA2 API')
input_text=st.text_input("Search the topic you want")


# ollama llama2 llm
llm=OllamaLLM(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))