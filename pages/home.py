import streamlit as st
import base64

# Fungsi untuk membuat link unduhan dataset
def download_link(file_path, file_name, link_text):
    with open(file_path, "rb") as file:
        b64 = base64.b64encode(file.read()).decode()  # Encode file ke base64
    href = f'<a href="data:file/csv;base64,{b64}" download="{file_name}">{link_text}</a>'
    return href

def run():
    st.title("House Price Prediction App")
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
    # Tampilkan tautan unduhan dataset
    st.markdown(download_link("data/california_housing.csv", "california_housing.csv", "📥 Download Dataset Contoh"), unsafe_allow_html=True)
