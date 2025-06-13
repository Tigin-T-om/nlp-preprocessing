import spacy
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
nltk.download('punkt')

stemmer = PorterStemmer()
text = "Canada-based Pakistani extradited to US; curfew declared in downtown LA; and more. The news includes a murder case, a foiled terror plot, protests, and delays in a space mission."
tokens = word_tokenize(text)

stems = [stemmer.stem(token) for token in tokens]
print("spaCy (NLTK-based) Stemming:", stems)
