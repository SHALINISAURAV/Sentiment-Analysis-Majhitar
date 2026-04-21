import pandas as pd
import re
import nltk
import os
from nltk.corpus import stopwords

# safe stopwords load
try:
    stop_words = set(stopwords.words('english'))
except:
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))


def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-zA-Z ]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    
    words = text.split()
    words = [w for w in words if w not in stop_words]
    
    return " ".join(words)


def get_sentiment(rating):
    if rating >= 4:
        return "positive"
    elif rating == 3:
        return "neutral"
    else:
        return "negative"


def load_and_process():
    # FIXED PATH (works locally + cloud)
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    file_path = os.path.join(base_dir, "data", "reviews.csv")

    df = pd.read_csv(file_path)

    df['clean_review'] = df['review'].apply(clean_text)
    df['sentiment'] = df['rating'].apply(get_sentiment)

    return df
