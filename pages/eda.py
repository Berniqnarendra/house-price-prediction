import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def run():
    st.title("Exploratory Data Analysis (EDA)")

    if "dataset" in st.session_state:
        df = st.session_state["dataset"]

        st.write("Dataset:")
        st.dataframe(df)

        st.subheader("Statistik Deskriptif")
        st.write(df.describe())

        st.subheader("Korelasi Antar Fitur")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)
    else:
        st.warning("Silakan unggah dataset terlebih dahulu.")
