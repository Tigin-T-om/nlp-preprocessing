import spacy
nlp = spacy.load("en_core_web_sm")

text = "Mayor imposes ‘days-long’ curfew, calls on Donald Trump to ‘end raids’ | 10 quick updates. A curfew has been imposed in downtown LA after a night of looting and chaos, with over 100 arrests."
doc = nlp(text)

filtered = [token.text for token in doc if not token.is_stop]
print("Spacy Stopword Removal: ", filtered)