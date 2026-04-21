import streamlit as st
import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.preprocess import load_and_process, clean_text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load and process data
df = load_and_process()

X = df['clean_review']
y = df['sentiment']

# Train model (on app start)
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

model = LogisticRegression(max_iter=200, class_weight='balanced')
model.fit(X_vec, y)

# UI
st.title("🍽️ Restaurant Sentiment Analyzer")
st.write("Enter a review and get sentiment prediction")

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
