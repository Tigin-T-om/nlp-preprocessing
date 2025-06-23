import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Input documents
documents = [
    "Sam eats pizza after football",
    "Pizza and Burger are delicious",
    "Ram play football on sunday",
    "Burger and pizza after game",
    "She Loves Pizza and Tennis"
]

# Bag-of-Words
bow_vectorizer = CountVectorizer()
X_bow = bow_vectorizer.fit_transform(documents)
df_bow = pd.DataFrame(X_bow.toarray(), columns=bow_vectorizer.get_feature_names_out())

# TF-IDF
tfidf_vectorizer = TfidfVectorizer()
X_tfidf = tfidf_vectorizer.fit_transform(documents)
df_tfidf = pd.DataFrame(X_tfidf.toarray(), columns=tfidf_vectorizer.get_feature_names_out())

# WordClouds for individual sentences
fig, axs = plt.subplots(5, 2, figsize=(14, 16))

# BoW WordClouds
for i, row in df_bow.iterrows():
    word_freq = row.to_dict()
    wc = WordCloud(background_color='white').generate_from_frequencies(word_freq)
    axs[i, 0].imshow(wc, interpolation='bilinear')
    axs[i, 0].set_title(f'BoW - Sentence {i+1}')
    axs[i, 0].axis('off')

# TF-IDF WordClouds
for i, row in df_tfidf.iterrows():
    word_freq = row.to_dict()
    wc = WordCloud(background_color='white').generate_from_frequencies(word_freq)
    axs[i, 1].imshow(wc, interpolation='bilinear')
    axs[i, 1].set_title(f'TF-IDF - Sentence {i+1}')
    axs[i, 1].axis('off')

plt.tight_layout()
plt.show()

# WordClouds for entire document
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
bow_total = df_bow.sum().to_dict()
tfidf_total = df_tfidf.sum().to_dict()

ax1.imshow(WordCloud(background_color='white').generate_from_frequencies(bow_total), interpolation='bilinear')
ax1.set_title("BoW - Entire Document")
ax1.axis('off')

ax2.imshow(WordCloud(background_color='white').generate_from_frequencies(tfidf_total), interpolation='bilinear')
ax2.set_title("TF-IDF - Entire Document")
ax2.axis('off')

plt.tight_layout()
plt.show()

# Cosine similarity matrix using BoW
cos_sim_bow = cosine_similarity(X_bow)
plt.figure(figsize=(6, 5))
sns.heatmap(cos_sim_bow, annot=True, cmap="YlGnBu", xticklabels=[f'Doc {i+1}' for i in range(5)],
            yticklabels=[f'Doc {i+1}' for i in range(5)])
plt.title("Cosine Similarity Matrix (BoW)")
plt.show()

# Cosine similarity matrix using TF-IDF
cos_sim_tfidf = cosine_similarity(X_tfidf)
plt.figure(figsize=(6, 5))
sns.heatmap(cos_sim_tfidf, annot=True, cmap="YlOrBr", xticklabels=[f'Doc {i+1}' for i in range(5)],
            yticklabels=[f'Doc {i+1}' for i in range(5)])
plt.title("Cosine Similarity Matrix (TF-IDF)")
plt.show()
