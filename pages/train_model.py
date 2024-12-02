import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def run():
    st.title("Train Model")

    if "dataset" in st.session_state:
        df = st.session_state["dataset"]
        X = df.iloc[:, :-1]  # Semua kolom kecuali target
        y = df.iloc[:, -1]   # Kolom target

        # Split dataset
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Pilihan model
        st.subheader("Pilih Model")
        model_option = st.selectbox(
            "Pilih model machine learning untuk training:",
            ["Linear Regression", "Decision Tree", "Random Forest"]
        )

        # Inisialisasi model berdasarkan pilihan
        if model_option == "Linear Regression":
            model = LinearRegression()
        elif model_option == "Decision Tree":
            model = DecisionTreeRegressor(random_state=42)
        elif model_option == "Random Forest":
            model = RandomForestRegressor(random_state=42)

        # Training model
        if st.button("Train Model"):
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)

            # Menampilkan hasil training
            st.write(f"Model yang digunakan: **{model_option}**")
            st.write(f"Mean Squared Error: **{mse:.2f}**")

            # Simpan model di session state
            st.session_state["model"] = model
            st.success("Model berhasil dilatih dan disimpan!")
    else:
        st.warning("Silakan unggah dataset terlebih dahulu.")
