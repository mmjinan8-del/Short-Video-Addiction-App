import streamlit as st
import pandas as pd
import pickle

st.title("Short Video Addiction Prediction App")

st.write("This app predicts the level of short-video addiction using a machine learning model.")

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

gender = st.selectbox("Gender", ["Female", "Male"])

age_group = st.selectbox(
    "Age Group",
    ["Under 18", "18-24", "25-34", "35+"]
)

daily_hours = st.selectbox(
    "Daily Watching Hours",
    ["Less than 1 hour", "1 - 3 hours", "3 - 5 hours", "More than 5 hours"]
)

open_freq = st.selectbox(
    "How many times do you open short-video apps per hour?",
    ["1 - 2 times", "3 - 5 times", "More than 5 times", "Constantly"]
)

reduce_try = st.selectbox(
    "Have you tried to reduce your short-video usage?",
    ["I haven't tried", "I tried and succeeded", "I tried but failed"]
)

time_loss = st.selectbox(
    "Do you lose track of time once you start scrolling?",
    ["Rarely", "Sometimes", "Often", "Always"]
)

hard_stop = st.selectbox(
    "Do you find it difficult to stop watching even with urgent tasks?",
    ["Rarely", "Sometimes", "Often", "Always"]
)

long_vid_bored = st.selectbox(
    "Do you feel bored quickly when watching long-form videos?",
    ["No", "Yes"]
)

escape_use = st.selectbox(
    "Do you use short videos to escape from stress or boredom?",
    ["Rarely", "Sometimes", "Often", "Always"]
)

sleep_impact = st.selectbox(
    "Has your sleep quality or bedtime been affected?",
    ["Not at all", "Sometimes", "Yes, significantly"]
)

# Convert inputs to numbers
input_data = pd.DataFrame([[
    0 if gender == "Female" else 1,
    ["Under 18", "18-24", "25-34", "35+"].index(age_group),
    ["Less than 1 hour", "1 - 3 hours", "3 - 5 hours", "More than 5 hours"].index(daily_hours),
    ["1 - 2 times", "3 - 5 times", "More than 5 times", "Constantly"].index(open_freq),
    ["I haven't tried", "I tried and succeeded", "I tried but failed"].index(reduce_try),
    ["Rarely", "Sometimes", "Often", "Always"].index(time_loss),
    ["Rarely", "Sometimes", "Often", "Always"].index(hard_stop),
    0 if long_vid_bored == "No" else 1,
    ["Rarely", "Sometimes", "Often", "Always"].index(escape_use),
    ["Not at all", "Sometimes", "Yes, significantly"].index(sleep_impact)
]])

if st.button("Predict"):
    prediction = model.predict(input_data)

    st.subheader("Prediction Result")

    if prediction[0] == 0:
        st.success("Not Addicted")
    elif prediction[0] == 1:
        st.warning("At Risk")
    else:
        st.error("Addicted")