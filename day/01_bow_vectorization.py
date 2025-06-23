from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

documents = [
    "Natural Language processing is fascinating.",
    "Machine Learning includes natural language preprocessing.",
    "Text analysis is part of natural language processing.",
    "Bag of words and Tf-IDF are text vectorization techiniques."
]

vectorizer = CountVectorizer()
X_bow = vectorizer.fit_transform(documents)

df_bow = pd.DataFrame(X_bow.toarray(), columns=vectorizer.get_feature_names_out())
print("Bag of words Matrix: ")
print(df_bow)