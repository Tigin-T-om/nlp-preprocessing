import spacy
nlp = spacy.load("en_core_web_sm")

text = "China stocks near 3-week high as Sino-US trade truce sparks optimism. Chinese stocks surged due to optimism surrounding progress in U.S.-China trade negotiations."
doc = nlp(text)

tokens = [token.text for token in doc]
print("spaCy Tokenization:", tokens)
