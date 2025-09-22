import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
text = "More bad news for Turkey and Pakistan as Azerbaijan inks deal with India… Azerbaijan has made a secret oil deal with India, which is a setback for Turkey who had broken ties with Israel."

tokens = word_tokenize(text)
filtered = [token for token in tokens if token.lower() not in stop_words]
print("NLTK Stopword Removal: ", filtered)