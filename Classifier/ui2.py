import sys
import os
import streamlit as st

# Add the parent directory to sys.path if disease_model is not installed as a package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crop_classifier import predict_disease

uploaded_file = st.file_uploader("Upload a leaf image", type=["jpg", "jpeg", "png"])
if uploaded_file:
    label, confidence = predict_disease(uploaded_file)
    st.success(f"Detected: {label} with {confidence}% confidence")
