# Install libraries if not installed
# !pip install nltk spacy

import nltk
import spacy
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download necessary resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

corpus = [
    "The quick brown fox jumps over the lazy dog.",
    "Artificial Intelligence and Machine Learning are transforming industries.",
    "Natural Language Processing makes machines understand human language."
]

# Initialize tools
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

print("========== TEXT PRE-PROCESSING ==========\n")

for sentence in corpus:
    print(f"Original Sentence: {sentence}\n")

    # 1. Tokenization (NLTK)
    tokens = word_tokenize(sentence)
    print(f"Tokens: {tokens}")

    # 2. Stop word removal
    filtered_tokens = [w for w in tokens if w.lower() not in stop_words]
    print(f"After Stop word Removal: {filtered_tokens}")

    # 3. Stemming (NLTK)
    stemmed_tokens = [stemmer.stem(w) for w in filtered_tokens]
    print(f"After Stemming: {stemmed_tokens}")

    # 4. Lemmatization (NLTK)
    lemmatized_tokens = [lemmatizer.lemmatize(w) for w in filtered_tokens]
    print(f"After Lemmatization (NLTK): {lemmatized_tokens}")

    # 5. Lemmatization using SpaCy (optional - for comparison)
    doc = nlp(sentence)
    spacy_lemmas = [token.lemma_ for token in doc if token.text.lower() not in stop_words]
    print(f"After Lemmatization (SpaCy): {spacy_lemmas}\n")

    print("-" * 60)
