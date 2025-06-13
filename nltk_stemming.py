import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
nltk.download('punkt')

stemmer = PorterStemmer()
text = "Transfer rumors, news: Liverpool close in on Wirtz Liverpool is reportedly close to signing Bayer Leverkusen’s Florian Wirtz, breaking their club record for the transfer."

tokens = word_tokenize(text)
stems = [stemmer.stem(token) for token in tokens]
print("NLTK Stemming:", stems)
