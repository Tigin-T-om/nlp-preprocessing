from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

# Load previously saved BoW and TF-IDF data (manually paste from above if needed)
# Sample: Use same data as above
word_freq_bow = {
    'natural': 3, 'language': 3, 'processing': 3,
    'machine': 1, 'learning': 1, 'includes': 1,
    'text': 2, 'analysis': 1, 'part': 1,
    'bag': 1, 'of': 1, 'words': 1, 'tfidf': 1, 'are': 1, 'vectorization': 1, 'techniques': 1
}

# BoW WordCloud
wc = WordCloud(width=800, height=400, background_color='white')
plt.figure(figsize=(10, 5))
plt.title("Bag-of-Words WordCloud")
plt.imshow(wc.generate_from_frequencies(word_freq_bow), interpolation="bilinear")
plt.axis("off")
plt.show()

# Use tf-idf values similarly (can be fetched from df_tfidf.sum().to_dict())
