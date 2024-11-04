import streamlit as st
import pandas as pd
import pickle

# Load the model
model_file_path = 'C:\\Users\\Sachin\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\Car-Price_prediction_model.pkl'
with open(model_file_path, 'rb') as file:
    model = pickle.load(file)

# Title of the app
st.title("Car Price Prediction App")

# User inputs
st.header("Enter Car Features")

# Input fields for car features (modify these according to your model's features)
make = st.selectbox("Make", ['Toyota', 'Honda', 'Ford', 'BMW', 'Tesla'])  # Example options
model_name = st.text_input("Model")
year = st.number_input("Year", min_value=2000, max_value=2023, value=2020)
mileage = st.number_input("Mileage (in km)", min_value=0, value=50000)
fuel_type = st.selectbox("Fuel Type", ['Petrol', 'Diesel', 'Electric', 'Hybrid'])
transmission = st.selectbox("Transmission", ['Manual', 'Automatic'])

# Button for prediction
if st.button("Predict Price"):
    # Prepare input for the model
    input_data = pd.DataFrame({
        'Make': [make],
        'Model': [model_name],
        'Year': [year],
        'Mileage': [mileage],
        'Fuel_Type': [fuel_type],
        'Transmission': [transmission]
    })

    # Make prediction
    predicted_price = model.predict(input_data)

    # Display the prediction
    st.subheader("Predicted Price:")
    st.write(f"${predicted_price[0]:,.2f}")

# Instructions for users
st.sidebar.header("Instructions")
st.sidebar.write("""
1. Select the car's make and fuel type from the dropdowns.
2. Enter the car model, year, and mileage.
3. Click on the "Predict Price" button to see the predicted price of the car.
""")
