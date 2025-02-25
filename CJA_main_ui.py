
import streamlit as st
import pandas as pd

st.title("Customer Journey Analysis")

uploaded_file = st.file_uploader("Upload Customer Behavior CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Preview of Uploaded Dataset:")
    st.write(df.head())
else:
    st.write("Upload a CSV file to start the analysis.")
