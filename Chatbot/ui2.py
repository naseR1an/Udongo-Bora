import streamlit as st
from prompt_templates import certification_prompt
from langchain.llms import Cohere  # or OpenAI, etc.

llm = Cohere()  # Initialize your model connection

region = st.text_input("Enter region:")
crop = st.text_input("Enter crop:")

if region and crop:
    filled_prompt = certification_prompt.format(region=region, crop=crop)
    response = llm.invoke(filled_prompt)
    st.success(response)