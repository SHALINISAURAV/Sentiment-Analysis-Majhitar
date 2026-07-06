# 🍽️ Sentiment Analysis of Restaurant Reviews (Majhitar, Sikkim)

<div align="center">

### 🧠 NLP-based sentiment classification system for real-world restaurant reviews

</div>

---

## 📌 Project Overview

This project applies **Natural Language Processing (NLP)** techniques to analyze customer reviews of restaurants in Majhitar, Sikkim.

The system classifies text reviews into:
- 😊 Positive  
- 😐 Neutral  
- 😡 Negative  

It also evaluates model performance using standard machine learning metrics.

---

## 🚀 Live Demo

👉 Try the application here:  
https://sentiment-analysis-majhitar-rt6lcycxzndimdes9rwqca.streamlit.app

---

## ✨ Key Features

- 🧹 Text preprocessing (cleaning, stopword removal, normalization)
- 📊 TF-IDF feature extraction
- 🤖 Logistic Regression classification model
- 📈 Model evaluation (Accuracy, Precision, Recall, F1-score)
- 🔥 Confusion matrix visualization
- 🌐 Interactive Streamlit web application
- ⚡ Real-time sentiment prediction

---

## 🧠 Tech Stack

- Python 🐍  
- Pandas, NumPy  
- Scikit-learn  
- NLTK  
- Matplotlib  
- Streamlit  

---

## 📂 Project Structure

```
SENTIMENT-ANALYSIS-MAJHITAR
├── app/
│   └── app.py
├── data/
│   └── reviews.csv
├── models/
│   └── model.pkl
├── notebooks/
│   └── analysis.ipynb
├── outputs/
│   ├── results.txt
│   ├── Sentiment_Distribution.png
│   └── confusion_matrix.png
├── src/
│   ├── preprocess.py
│   ├── train.py
│   └── evaluate.py
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

```bash
git clone https://github.com/SHALINISAURAV/sentiment-analysis-majhitar.git
cd sentiment-analysis-majhitar
pip install -r requirements.txt
```

---

## ▶️ How to Run

### Train Model
```bash
python src/train.py
```

### Evaluate Model
```bash
python src/evaluate.py
```

### Run App
```bash
streamlit run app/app.py
```

---

## 📊 Model Performance

- Model: Logistic Regression  
- Features: TF-IDF Vectorization  
- Baseline Accuracy: ~46% (depends on dataset quality and size)

---

## 📈 Results

- Evaluation metrics stored in `outputs/results.txt`
- Visual insights via confusion matrix and sentiment distribution plots

---

## 🧪 Sample Predictions

| Review | Sentiment |
|--------|------------|
| Amazing food and service | 😊 Positive |
| It was okay | 😐 Neutral |
| Very bad experience | 😡 Negative |

---

## ⚠️ Challenges

- Limited dataset size affecting accuracy  
- Class imbalance in sentiment labels  
- Deployment path and import issues  
- Model serialization (pickle handling)

---

## 🚀 Future Improvements

- Upgrade to BERT / transformer-based models  
- Improve dataset size and quality  
- Hyperparameter tuning  
- Deploy as full-stack app (FastAPI + frontend UI)

---

## 👨‍💻 Author

**Shalini Saurav**

---

## ⭐ Support

If you found this useful, consider starring the repository!
