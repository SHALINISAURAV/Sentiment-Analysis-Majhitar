from src.preprocess import load_and_process
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import os

df = load_and_process()

X = df['clean_review']
y = df['sentiment']

vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.2, random_state=42)

# ✅ FIX: balanced model
model = LogisticRegression(max_iter=200, class_weight='balanced')
model.fit(X_train, y_train)

# Save model
os.makedirs("models", exist_ok=True)
pickle.dump((model, vectorizer), open("models/model.pkl", "wb"))

print("Model trained successfully")
