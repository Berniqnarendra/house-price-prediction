import streamlit as st
from streamlit_option_menu import option_menu

# Konfigurasi halaman utama
st.set_page_config(page_title="House Price Prediction", layout="wide")

# Sidebar navigasi
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["Home", "Upload Dataset", "EDA", "Train Model", "Predict"],
        icons=["house", "cloud-upload", "bar-chart", "robot", "clipboard-check"],
        default_index=0,
    )

# Navigasi ke halaman yang dipilih
if selected == "Home":
    from pages import home
    home.run()
elif selected == "Upload Dataset":
    from pages import upload_dataset
    upload_dataset.run()
elif selected == "EDA":
    from pages import eda
    eda.run()
elif selected == "Train Model":
    from pages import train_model
    train_model.run()
elif selected == "Predict":
    from pages import predict
    predict.run()
