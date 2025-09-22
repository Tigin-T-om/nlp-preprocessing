import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()
text = "COVID-19 Cases In India: Active Cases Jump To 7121 Active cases have jumped to 7121 with 306 new infections and 6 deaths recorded on Wednesday."

tokens = word_tokenize(text)
lemmas = [lemmatizer.lemmatize(token) for token in tokens]
print("NLTK Lemmatization:", lemmas)
