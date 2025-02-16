
import pickle
import streamlit as st
import pandas as pd

# load the file that contains the model (model.pkl)
with open("model.pkl", "rb") as f:
  model = pickle.load(f)

# give the Streamlit app page a title
st.title("Resurant Revenue Predictor")

# input widget for getting user values for X (feature matrix value)
Seating_Capacity = st.slider("Seating Capacity", min_value=0, max_value=100, value=20)
Average_Meal_Price= st.slider("Average Meal Price", min_value=0, max_value=100, value=20)
Marketing_Budget = st.slider("Marketing Budget", min_value=0, max_value=10000, value=20)



# After selesting Revenue, the user then submits the price value
if st.button("Predict"):
  # take the price value, and format the value the right way
  prediction = model.predict([[Seating_Capacity, Average_Meal_Price, Marketing_Budget]])[0].round(2)
  st.write("Expected Revenue ", prediction, "thousand dollars")
