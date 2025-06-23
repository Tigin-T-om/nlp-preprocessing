from textblob import TextBlob
from deep_translator import GoogleTranslator

# Create a TextBlob object
text = "I really enjoy reading your blog. It's insightful and well-written."
blob = TextBlob(text)

# Sentiment Analysis
print("Sentiment:", blob.sentiment)

# Noun Phrases
print("Noun Phrases:", blob.noun_phrases)

# Tokenization
print("Words:", blob.words)
print("Sentences:", blob.sentences)

# Foreign text
foreign_text = "C'est une belle journée"

try:
    # Translation (auto-detect language internally)
    translated = GoogleTranslator(source='auto', target='en').translate(foreign_text)
    print("Translation:", translated)
except Exception as e:
    print("Translation failed:", e)
