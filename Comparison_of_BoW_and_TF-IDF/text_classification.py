import pandas as pd
import numpy as np
import re
import string
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

# Load dataset
df = pd.read_csv("sentiment_dataset.csv")

# Basic info
print("Dataset Shape:", df.shape)
print("Class Distribution:\n", df['sentiment'].value_counts())

# Visualize sentiment distribution
plt.figure(figsize=(6, 4))
sns.countplot(x='sentiment', data=df, palette='Set2')
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()

# Preprocessing function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'<.*?>', ' ', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\d+', '', text)
    return text

# Apply cleaning
df['clean_review'] = df['review'].apply(clean_text)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    df['clean_review'], df['sentiment'], test_size=0.2, random_state=42
)

# ========== Bag-of-Words ==========
bow_vectorizer = CountVectorizer(stop_words='english')
X_train_bow = bow_vectorizer.fit_transform(X_train)
X_test_bow = bow_vectorizer.transform(X_test)

bow_model = LogisticRegression(max_iter=1000)
bow_model.fit(X_train_bow, y_train)
y_pred_bow = bow_model.predict(X_test_bow)

print("\n🔤 Bag-of-Words Results:")
print("Accuracy:", accuracy_score(y_test, y_pred_bow))
print(classification_report(y_test, y_pred_bow))

# Confusion Matrix - BoW
cm_bow = confusion_matrix(y_test, y_pred_bow, labels=bow_model.classes_)
plt.figure(figsize=(5, 4))
sns.heatmap(cm_bow, annot=True, fmt='d', cmap='Blues', xticklabels=bow_model.classes_, yticklabels=bow_model.classes_)
plt.title("BoW Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# ========== TF-IDF ==========
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
X_test_tfidf = tfidf_vectorizer.transform(X_test)

tfidf_model = LogisticRegression(max_iter=1000)
tfidf_model.fit(X_train_tfidf, y_train)
y_pred_tfidf = tfidf_model.predict(X_test_tfidf)

print("\n📘 TF-IDF Results:")
print("Accuracy:", accuracy_score(y_test, y_pred_tfidf))
print(classification_report(y_test, y_pred_tfidf))

# Confusion Matrix - TF-IDF
cm_tfidf = confusion_matrix(y_test, y_pred_tfidf, labels=tfidf_model.classes_)
plt.figure(figsize=(5, 4))
sns.heatmap(cm_tfidf, annot=True, fmt='d', cmap='Greens', xticklabels=tfidf_model.classes_, yticklabels=tfidf_model.classes_)
plt.title("TF-IDF Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
