from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import seaborn as sns
import matplotlib.pyplot as plt

documents = [
    "Natural language processing is fascinating.",
    "Machine learning includes natural language processing.",
    "Text analysis is part of natural language processing.",
    "Bag of Words and TF-IDF are text vectorization techniques."
]

tfidf_vectorizer = TfidfVectorizer()
X_tfidf = tfidf_vectorizer.fit_transform(documents)

cos_sim = cosine_similarity(X_tfidf)

sns.heatmap(cos_sim, annot=True, cmap="YlGnBu", xticklabels=False, yticklabels=False)
plt.title("TF-IDF Cosine Similarity Between Documents")
plt.show()
