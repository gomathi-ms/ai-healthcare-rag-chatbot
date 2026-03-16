import streamlit as st
import requests

st.title("AI Healthcare Assistant")

question = st.text_input("Ask a medical question")

if st.button("Submit"):

    response = requests.get(
        "http://localhost:8000/chat",
        params={"query": question}
    )

    st.write(response.json()["response"])
