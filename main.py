import streamlit as st  # For creating web interface
import pandas as pd  # For data manipulation
import datetime  # For handling dates
import csv  # For reading and writing CSV file
import os  # For file operations
import matplotlib.pyplot as plt  # For creating bar chart

# Define the file name for storing mood data
MOOD_FILE = "mood_log.csv"

# Function to read mood data from the CSV file
def load_mood_data():
    # Check if the file exists
    if not os.path.exists(MOOD_FILE):
        # If no file, create empty DataFrame with columns
        return pd.DataFrame(columns=["Date", "Mood"])
    # Read and return existing mood data
    return pd.read_csv(MOOD_FILE)

# Function to add new mood entry to CSV file
def save_mood_data(date, mood):
    # Open file in append mode
    with open(MOOD_FILE, "a") as file:
        # Create CSV writer
        writer = csv.writer(file)
        # Add new mood entry
        writer.writerow([date, mood])

# Streamlit app title
st.title("Mood Tracker")

# Get today's date
today = datetime.date.today()

# Create subheader for mood input
st.subheader("How are you feeling today?")

# Create dropdown for mood selection
mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry", "Neutral"])

# Create button to save mood
if st.button("Log Mood"):
    # Save mood when button is clicked
    save_mood_data(today, mood)
    # Show success message
    st.success("Mood Logged Successfully!")

# Load existing mood data
data = load_mood_data()

# If there is data to display
if not data.empty:
    # Create section for Visualization
    st.subheader("Mood Trends Over Time")

    # Convert date strings to datetime objects
    data["Date"] = pd.to_datetime(data["Date"])

    # Count frequency of each mood
    mood_counts = data["Mood"].value_counts()

    # Create a Matplotlib bar chart
    fig, ax = plt.subplots()
    mood_counts.plot(kind="bar", ax=ax, color=["blue", "red", "green", "orange"])
    ax.set_xlabel("Mood")
    ax.set_ylabel("Frequency")
    ax.set_title("Mood Trends Over Time")
    ax.grid(axis="y", linestyle="--", alpha=0.7)

    # Display the Matplotlib chart in Streamlit
    st.pyplot(fig)
