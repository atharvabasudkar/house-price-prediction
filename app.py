import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("house_price_model.joblib")

# App Title
st.title("🏠 Boston House Price Prediction App")

st.write("Enter the house details below to predict the house price.")

# User Inputs
crime_rate = st.number_input(
    "Crime Rate",
    min_value=0.0,
    step=0.1
)

residential_land = st.number_input(
    "Residential Land Zoning Percentage",
    min_value=0.0,
    step=0.1
)

industrial_area = st.number_input(
    "Industrial Area Percentage",
    min_value=0.0,
    step=0.1
)

river_location = st.selectbox(
    "Near Charles River?",
    [0, 1]
)

nitric_oxide = st.number_input(
    "Nitric Oxide Concentration",
    min_value=0.0,
    step=0.01
)

rooms = st.number_input(
    "Average Number of Rooms",
    min_value=0.0,
    step=0.1
)

old_houses = st.number_input(
    "Percentage of Old Houses",
    min_value=0.0,
    step=0.1
)

distance = st.number_input(
    "Distance to Employment Centers",
    min_value=0.0,
    step=0.1
)

highway_access = st.number_input(
    "Accessibility to Highways",
    min_value=0.0,
    step=1.0
)

property_tax = st.number_input(
    "Property Tax Rate",
    min_value=0.0,
    step=1.0
)

teacher_ratio = st.number_input(
    "Pupil Teacher Ratio",
    min_value=0.0,
    step=0.1
)

black_population = st.number_input(
    "Black Population Index",
    min_value=0.0,
    step=0.1
)

lower_status = st.number_input(
    "Lower Status Population Percentage",
    min_value=0.0,
    step=0.1
)

# Prediction Button
if st.button("Predict House Price"):

    features = np.array([[
        crime_rate,
        residential_land,
        industrial_area,
        river_location,
        nitric_oxide,
        rooms,
        old_houses,
        distance,
        highway_access,
        property_tax,
        teacher_ratio,
        black_population,
        lower_status
    ]])

    prediction = model.predict(features)

    st.success(
        f"🏡 Predicted House Price: ${prediction[0] * 1000:.2f}"
    )