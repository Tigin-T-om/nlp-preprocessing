from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

documents = [
    "Natural language processing is fascinating.",
    "Machine learning includes natural language processing.",
    "Text analysis is part of natural language processing.",
    "Bag of Words and TF-IDF are text vectorization techniques."
]

tfidf_vectorizer = TfidfVectorizer()
X_tfidf = tfidf_vectorizer.fit_transform(documents)

df_tfidf = pd.DataFrame(X_tfidf.toarray(), columns=tfidf_vectorizer.get_feature_names_out())
print("TF-IDF Matrix:")
print(df_tfidf)
