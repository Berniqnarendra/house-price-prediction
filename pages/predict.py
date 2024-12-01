import streamlit as st
import numpy as np

def run():
    st.title("Predict House Prices")

    if "model" in st.session_state:
        model = st.session_state["model"]

        st.markdown("Masukkan data untuk prediksi:")
        MedInc = st.number_input("Median Income", min_value=0.0)
        HouseAge = st.number_input("House Age", min_value=0.0)
        AveRooms = st.number_input("Average Rooms", min_value=0.0)
        AveBedrms = st.number_input("Average Bedrooms", min_value=0.0)
        Population = st.number_input("Population", min_value=0.0)
        AveOccup = st.number_input("Average Occupancy", min_value=0.0)
        Latitude = st.number_input("Latitude", min_value=-90.0, max_value=90.0)
        Longitude = st.number_input("Longitude", min_value=-180.0, max_value=180.0)

        if st.button("Predict"):
            input_data = np.array([[MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude]])
            prediction = model.predict(input_data)
            st.success(f"Prediksi harga rumah: ${prediction[0]:.2f}")
    else:
        st.warning("Silakan latih model terlebih dahulu.")
