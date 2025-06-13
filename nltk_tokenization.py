import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

text = " Sonam Accused Of Black Magic, Zara Store Looted In LA & Other Top Stories. The digest covers Raja Raghuvanshi’s murder, Los Angeles protests, and other top stories."

tokens = word_tokenize(text)
print("NLTK Tokenization:", tokens)
