
import pickle
import streamlit as st
import pandas as pd

# load the file that contains the model (model.pkl)
with open("model.pkl", "rb") as f:
  model = pickle.load(f)

# give the Streamlit app page a title
st.title("Resurant Revenue Predictor")

# input widget for getting user values for X (feature matrix value)
Revenue = st.slider("Revenue", min_value=0, max_value=100, value=20)
Seating_Capacity = st.slider("Seating Capacity", min_value=0, max_value=100, value=20)
Average_Meal_Price= st.slider("Average Meal Price", min_value=0, max_value=100, value=20)
Marketing_Budget = st.slider("Marketing Budget", min_value=0, max_value=100, value=20)
Social_Media_Followers = st.slider("Social Media Followers", min_value=0, max_value=100, value=20)
Chef_Experience_Years = st.slider(""Chef Experience Years"", min_value=0, max_value=100, value=20)

# After selesting Revenue, the user then submits the price value
if st.button("Predict"):
  # take the price value, and format the value the right way
  prediction = model.predict([[Revenue, Social_Media_Followers, Marketing_Budget, Average_Meal_Price, Chef_Experience_Years]])[0].round(2)
  st.write("Expected Revenue", prediction, "thousand dollars")
