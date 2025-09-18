# CADL4: Topic Modeling with LDA (Latent Dirichlet Allocation)

import nltk
import spacy
from nltk.corpus import stopwords
from gensim import corpora
from gensim.models import LdaModel
import pyLDAvis.gensim_models as gensimvis
import pyLDAvis
import pandas as pd

# -----------------------------
# Step 1: Download resources
# -----------------------------
nltk.download("stopwords")
nlp = spacy.load("en_core_web_sm")
stop_words = set(stopwords.words("english"))

# -----------------------------
# Step 2: Sample Corpus (replace with your dataset if needed)
# -----------------------------
corpus = [
    "Artificial Intelligence and Machine Learning are transforming industries.",
    "Natural Language Processing allows computers to understand human language.",
    "Deep Learning is a subset of Machine Learning that uses neural networks.",
    "Climate change impacts agriculture, economy, and global health.",
    "Researchers are working on renewable energy solutions to combat climate change.",
    "Advancements in biotechnology are improving healthcare treatments."
]

# -----------------------------
# Step 3: Preprocessing (tokenization, stopword removal, lemmatization)
# -----------------------------
def preprocess(text):
    doc = nlp(text.lower())
    tokens = [
        token.lemma_
        for token in doc
        if token.is_alpha and token.lemma_ not in stop_words
    ]
    return tokens

processed_corpus = [preprocess(doc) for doc in corpus]

print("========== Preprocessed Corpus ==========")
for i, doc in enumerate(processed_corpus):
    print(f"Doc {i+1}: {doc}")

# -----------------------------
# Step 4: Dictionary & Document-Term Matrix
# -----------------------------
dictionary = corpora.Dictionary(processed_corpus)
doc_term_matrix = [dictionary.doc2bow(text) for text in processed_corpus]

# -----------------------------
# Step 5: Train LDA Model
# -----------------------------
lda_model = LdaModel(
    corpus=doc_term_matrix,
    id2word=dictionary,
    num_topics=3,       # Number of topics
    random_state=42,
    passes=10
)

print("\n========== LDA Topics ==========")
topics = lda_model.print_topics(num_words=5)
for idx, topic in topics:
    print(f"Topic {idx+1}: {topic}")

# Store topics in DataFrame (for GitHub/Moodle documentation)
df_topics = pd.DataFrame(
    [[idx+1, topic] for idx, topic in topics],
    columns=["Topic #", "Top Words"]
)
print("\nTopics DataFrame:\n", df_topics)

# -----------------------------
# Step 6: Visualization
# -----------------------------
lda_vis = gensimvis.prepare(lda_model, doc_term_matrix, dictionary)
pyLDAvis.save_html(lda_vis, "lda_visualization.html")

print("\n✅ LDA visualization saved as lda_visualization.html — open it in your browser.")
