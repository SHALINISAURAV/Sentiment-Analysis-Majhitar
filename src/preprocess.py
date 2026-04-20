import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-zA-Z ]", "", text)
    words = text.split()
    words = [w for w in words if w not in stopwords.words('english')]
    return " ".join(words)

def get_sentiment(rating):
    if rating >= 4:
        return "positive"
    elif rating == 3:
        return "neutral"
    else:
        return "negative"

def load_and_process():
    df = pd.read_csv("data/reviews.csv")  # ✅ FIXED PATH

    df['clean_review'] = df['review'].apply(clean_text)
    df['sentiment'] = df['rating'].apply(get_sentiment)

    return df
