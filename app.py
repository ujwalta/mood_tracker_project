import streamlit as st
import pandas as pd
import random
import os
from datetime import datetime
import matplotlib.pyplot as plt


DATA_FILE = "mood_data.csv"


if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["Date", "Mood", "Quote"])
    df.to_csv(DATA_FILE, index=False)

df = pd.read_csv(DATA_FILE)

quotes = {
    "Happy": [
        "Happiness is a journey, not a destination. 😊",
        "Smile, it’s contagious! 😄"
    ],
    "Sad": [
        "This too shall pass. 🌧️",
        "Every storm runs out of rain. 🌦️"
    ],
    "Motivated": [
        "Dream big, work hard! 💪",
        "Push yourself, because no one else is going to do it for you. 🚀"
    ],
    "Tired": [
        "Rest if you must, but never quit. 💤",
        "Even slow progress is progress. ⏳"
    ]
}

st.title("📝 Mood & Quote Tracker")

mood = st.selectbox("Select your mood today:", ["Happy", "Sad", "Motivated", "Tired"])
if st.button("Get Quote"):
    quote = random.choice(quotes[mood])
    st.success(f"{quote}")

    new_entry = pd.DataFrame({
        "Date": [datetime.now().date()],
        "Mood": [mood],
        "Quote": [quote]
    })
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)


st.subheader("📊 Mood History")
if not df.empty:
    mood_counts = df["Mood"].value_counts()
    plt.figure(figsize=(6,4))
    plt.bar(mood_counts.index, mood_counts.values, color=["yellow","blue","green","gray"])
    plt.xlabel("Mood")
    plt.ylabel("Count")
    plt.title("Mood Frequency")
    st.pyplot(plt)
else:
    st.info("No mood entries yet. Add your mood above!")
