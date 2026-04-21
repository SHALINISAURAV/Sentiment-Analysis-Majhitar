from src.preprocess import load_and_process
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle
import os

df = load_and_process()

X = df['clean_review']
y = df['sentiment']

# ✅ improved vectorizer
vectorizer = TfidfVectorizer(ngram_range=(1,2), max_features=500)
X_vec = vectorizer.fit_transform(X)

# ✅ stratified split
X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.2, random_state=42, stratify=y)

# ✅ balanced model
model = LogisticRegression(max_iter=200, class_weight='balanced')
model.fit(X_train, y_train)

# evaluation
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# save
os.makedirs("models", exist_ok=True)
pickle.dump((model, vectorizer), open("models/model.pkl", "wb"))

print("Model trained successfully")
