import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
import pickle
import sys
import os

# allow import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.preprocess import clean_text

# load model + vectorizer (FIXED)
model, vectorizer = pickle.load(open("models/model.pkl", "rb"))

# UI
st.title("🍽️ Restaurant Sentiment Analyzer")
st.write("Example: 'food was amazing but service slow'")

user_input = st.text_area("Enter your review:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a review")
    else:
        cleaned = clean_text(user_input)
        input_vec = vectorizer.transform([cleaned])
        prediction = model.predict(input_vec)[0]

        if prediction == "positive":
            st.success("😊 Positive Review")
        elif prediction == "neutral":
            st.info("😐 Neutral Review")
        else:
            st.error("😡 Negative Review")
