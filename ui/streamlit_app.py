import streamlit as st
import requests

st.title("AI Autonomous Agent")

query = st.text_input("Ask the Agent")

if st.button("Run Agent"):
    res = requests.post(
        "http://localhost:8000/agent",
        json={"query": query}
    )
    st.write(res.json())