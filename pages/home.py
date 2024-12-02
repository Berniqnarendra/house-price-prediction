import streamlit as st

def run():
    st.title("House Price Prediction")
    st.markdown("""
    Selamat datang di aplikasi **Prediksi Harga Rumah** berbasis Machine Learning!  
    Aplikasi ini memungkinkan Anda untuk:
    - Mengunggah dataset rumah Anda.
    - Melakukan Exploratory Data Analysis (EDA).
    - Melatih model Machine Learning untuk prediksi harga rumah.
    - Membuat prediksi menggunakan model terlatih.

    #### Contoh Dataset
    Anda dapat mengunduh dataset contoh di sini:
    """)
    st.markdown(download_link("data/california_housing.csv", "california_housing.csv", "📥 Download Dataset Contoh"), unsafe_allow_html=True)
