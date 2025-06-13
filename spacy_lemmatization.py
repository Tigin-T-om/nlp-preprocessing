import spacy
nlp = spacy.load("en_core_web_sm")

text = "RT-PCR Test Mandatory For Ministers Meeting PM Modi Amid Rising COVID-19 Cases An RT-PCR test is now mandatory for ministers meeting PM Modi due to the rise in COVID-19 cases in the country."
doc = nlp(text)

lemmas = [token.lemma_ for token in doc]
print("Spacy Lemmatization: ", lemmas)

