import streamlit as st
import pandas as pd
import pickle
import os

# Page setup
st.set_page_config(page_title="🏏 IPL Match Winner Predictor", layout="centered")
st.title("🏆 IPL 2025 Match Predictor")
st.markdown("Predict the winner of an IPL 2025 match using match stats!")

# Load model
model_path = os.path.join("ML Notebook", "new_model.pkl")

try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("Model file not found. Please make sure 'ipl_model.pkl' exists in the 'models' folder.")
    st.stop()

# Team & city list
teams = [
    "Chennai Super Kings", "Mumbai Indians", "Royal Challengers Bangalore",
    "Kolkata Knight Riders", "Delhi Capitals", "Rajasthan Royals",
    "Sunrisers Hyderabad", "Punjab Kings", "Lucknow Super Giants", "Gujarat Titans"
]

cities = [
    "Mumbai", "Chennai", "Delhi", "Bangalore", "Hyderabad", "Kolkata", 
    "Ahmedabad", "Jaipur", "Lucknow", "Mohali"
]

# Inputs
batting_team = st.selectbox("Select Batting Team", teams)
bowling_team = st.selectbox("Select Bowling Team", [t for t in teams if t != batting_team])
city = st.selectbox("Match City", cities)

target = st.number_input("Target Score", min_value=1)
current_score = st.number_input("Current Score", min_value=0)
overs_done = st.number_input("Overs Completed", min_value=0.0, max_value=20.0, step=0.1)
wickets = st.slider("Wickets Lost", 0, 10)

# Derived features
balls_done = int(overs_done * 6)
balls_left = 120 - balls_done
runs_left = max(0, target - current_score)
wickets_left = 10 - wickets

current_run_rate = current_score / overs_done if overs_done > 0 else 0
required_run_rate = (runs_left * 6 / balls_left) if balls_left > 0 else 0

# Predict button
if st.button("Predict Match Winner"):

    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets_left': [wickets_left],
        'target': [target],
        'current_run_rate': [current_run_rate],
        'required_run_rate': [required_run_rate]
    })

    st.write("🔍 Match Situation:")
    st.write(input_df)

    try:
        prediction = model.predict(input_df)[0]
        st.success(f"🏁 Predicted Winner: **{prediction}**")
    except Exception as e:
        st.error(f"⚠️ Prediction failed: {e}")
