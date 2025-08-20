import streamlit as st
import requests
import time

API = "http://localhost:8000"

st.title("Order Book Replay")

if st.button("Start Replay"):
    requests.get(f"{API}/start")
if st.button("Pause Replay"):
    requests.get(f"{API}/pause")

speed = st.slider("Speed", 1, 10, 1)
requests.get(f"{API}/speed?s={speed}")

placeholder = st.empty()

while True:
    book = requests.get(f"{API}/book").json()
    with placeholder.container():
        st.subheader("Bids")
        st.write(book["bids"])
        st.subheader("Asks")
        st.write(book["asks"])
    time.sleep(0.5)
