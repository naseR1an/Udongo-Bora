import streamlit as st
# from cert_helper import get_certification_steps

st.header("📄 Organic Certification Advisor")

region = st.text_input("Enter your region (e.g. Kenya)")
crop = st.text_input("Enter your crop (e.g. Maize)")

if region and crop:
    steps = get_certification_steps(region, crop)
    st.info(steps)
