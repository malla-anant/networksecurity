import streamlit as st
import requests
import pandas as pd


st.markdown("""
    <style>
    h1 {
        font-size: 32px !important;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)


st.title("📡 Network Security Prediction App")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully!")
    st.dataframe(df.head())

if st.button("Predict"):
    if uploaded_file is None:
        st.error("Please upload a file before prediction.")
    else:
        # Send file to FastAPI
        with st.spinner("Processing... Please wait"):
            response = requests.post(
                "http://127.0.0.1:8000/predict",
                files={"file": (uploaded_file.name, uploaded_file.getvalue())}
            )

        if response.status_code != 200:
            st.error(f"Error: {response.text}")
        else:
            # Convert HTML table to DataFrame
            df = pd.read_html(response.text)[0]

            st.success("Prediction Successful!")

            # ---- FIX: Scrollable table with styling ----
            st.dataframe(
                df,
                height=600,
                use_container_width=True
            )

            # ---- Download Button ----
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                "Download Predictions as CSV",
                data=csv,
                file_name="predictions_output.csv",
                mime="text/csv"
            )
