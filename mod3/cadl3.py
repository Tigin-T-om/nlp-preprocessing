import spacy
from spacy import displacy
import pandas as pd

nlp = spacy.load("en_core_web_sm")

text = """
Google is hiring a Data Scientist in Bangalore.
The role requires knowledge of Python and Machine Learning.
John Doe previously worked at Microsoft and will be presenting his research
at the AI Conference 2025 in San Francisco.
"""

doc = nlp(text)

# Extract all entities
print("Named Entities:")
for ent in doc.ents:
    print((ent.text, ent.label_))

# Collect persons and orgs
persons = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
orgs = [ent.text for ent in doc.ents if ent.label_ == "ORG"]

# --- Fix: align lists by length ---
max_len = max(len(persons), len(orgs))

# pad shorter list with empty strings
persons += [""] * (max_len - len(persons))
orgs += [""] * (max_len - len(orgs))

# Create dataframe
df = pd.DataFrame({"Person": persons, "Organization": orgs})
print("\nStructured Table:")
print(df)

# Save table
df.to_csv("entities.csv", index=False)

# Generate HTML
html = displacy.render(doc, style="ent", page=True)
with open("ner_entities.html", "w", encoding="utf-8") as f:
    f.write(html)

print("\n✅ 'entities.csv' and 'ner_entities.html' generated.")
