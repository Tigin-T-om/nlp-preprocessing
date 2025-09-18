# CADL2: Feature Extraction (BoW & TF-IDF)

# Import necessary libraries
import nltk
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Download stopwords
nltk.download('stopwords')
from nltk.corpus import stopwords

# Sample dataset (Movie Reviews)
corpus = [
    "I loved the movie, it was fantastic!",
    "The film was boring and too long.",
    "What a great performance by the lead actor.",
    "I would not recommend this movie to anyone.",
    "An excellent plot and well-developed characters."
]

# Define English stopwords
stop_words = stopwords.words('english')

# -----------------------------
# Bag-of-Words (BoW)
# -----------------------------
print("========== Bag of Words ==========")

# Create CountVectorizer object with stopword removal
vectorizer = CountVectorizer(stop_words='english')

# Fit and transform corpus
X_bow = vectorizer.fit_transform(corpus)

# Convert BoW to DataFrame for readability
df_bow = pd.DataFrame(X_bow.toarray(), columns=vectorizer.get_feature_names_out())

print("Vocabulary:\n", vectorizer.get_feature_names_out())
print("\nBoW DataFrame:\n", df_bow)

# -----------------------------
# Term Frequency-Inverse Document Frequency (TF-IDF)
# -----------------------------
print("\n========== TF-IDF ==========")

# Create TfidfVectorizer object with stopword removal
tfidf = TfidfVectorizer(stop_words='english')

# Fit and transform corpus
X_tfidf = tfidf.fit_transform(corpus)

# Convert TF-IDF to DataFrame
df_tfidf = pd.DataFrame(X_tfidf.toarray(), columns=tfidf.get_feature_names_out())

print("Vocabulary:\n", tfidf.get_feature_names_out())
print("\nTF-IDF DataFrame:\n", df_tfidf.round(3))  # Round for readability
