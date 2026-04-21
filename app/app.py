import streamlit as st
import sys
import os

# fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.preprocess import load_and_process
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# load data
df = load_and_process()

X = df['clean_review']
y = df['sentiment']

# vectorize
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# train model
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
        from src.preprocess import clean_text
        cleaned = clean_text(user_input)
        input_vec = vectorizer.transform([cleaned])
        prediction = model.predict(input_vec)[0]

        if prediction == "positive":
            st.success("😊 Positive Review")
        elif prediction == "neutral":
            st.info("😐 Neutral Review")
        else:
            st.error("😡 Negative Review")        else:
            st.error("😡 Negative Review")
