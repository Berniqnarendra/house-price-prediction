import streamlit as st
import pandas as pd

def run():
    st.title("Upload Dataset")
    st.markdown("Unggah dataset Anda untuk digunakan di aplikasi ini.")

    uploaded_file = st.file_uploader("Upload file CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("Dataset berhasil diunggah:")
        st.dataframe(df)
        st.session_state["dataset"] = df  # Simpan dataset ke session state
    elif "dataset" not in st.session_state:
        # Load dataset default jika tidak ada unggahan
        default_path = "data/california_housing.csv"
        df = pd.read_csv(default_path)
        st.session_state["dataset"] = df
        st.write("Menggunakan dataset default:")
        st.dataframe(df)
