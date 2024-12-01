import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def run():
    st.title("Train Model")

    if "dataset" in st.session_state:
        df = st.session_state["dataset"]
        X = df.iloc[:, :-1]  # Semua kolom kecuali target
        y = df.iloc[:, -1]   # Kolom target

        # Split dataset
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Evaluate model
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)

        st.write(f"Model telah dilatih. Mean Squared Error: {mse:.2f}")
        st.session_state["model"] = model
    else:
        st.warning("Silakan unggah dataset terlebih dahulu.")
