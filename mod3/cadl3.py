# CADL3: Named Entity Recognition (NER) with spaCy

import spacy
import pandas as pd

# -----------------------------
# Step 1: Load spaCy Pre-trained Model
# -----------------------------
nlp = spacy.load("en_core_web_sm")

# -----------------------------
# Step 2: Sample Dataset (Unstructured Text)
# -----------------------------
corpus = [
    "Google has hired John Smith as a Software Engineer in California.",
    "Mary Johnson joined Microsoft as a Data Scientist in Seattle.",
    "Amazon appointed David Lee to lead its Cloud Computing division.",
    "Elon Musk announced a new project at Tesla headquarters in Texas.",
    "IBM is collaborating with Alice Brown to develop AI solutions."
]

# -----------------------------
# Step 3: Perform NER on the Dataset
# -----------------------------
entities = []
for sentence in corpus:
    parsed_doc = nlp(sentence)
    for ent in parsed_doc.ents:
        entities.append([sentence, ent.text, ent.label_])

# Convert to DataFrame for visualization
df_entities = pd.DataFrame(entities, columns=["Sentence", "Entity", "Label"])

print("========== Named Entities ==========")
print(df_entities)

# -----------------------------
# Step 4: Extract Persons & Organizations
# -----------------------------
person_org = []

for sentence in corpus:
    parsed_doc = nlp(sentence)
    persons = [ent.text for ent in parsed_doc.ents if ent.label_ == "PERSON"]
    orgs = [ent.text for ent in parsed_doc.ents if ent.label_ == "ORG"]

    # Pair each person with each org in the sentence
    for person in persons:
        for org in orgs:
            person_org.append([person, org])

# Convert to DataFrame
df_person_org = pd.DataFrame(person_org, columns=["Person", "Organization"])

print("\n========== Persons & Organizations ==========")
print(df_person_org)

# -----------------------------
# Step 5: (Optional) Extract Persons, Orgs & Locations
# -----------------------------
structured_info = []

for sentence in corpus:
    parsed_doc = nlp(sentence)
    persons = [ent.text for ent in parsed_doc.ents if ent.label_ == "PERSON"]
    orgs = [ent.text for ent in parsed_doc.ents if ent.label_ == "ORG"]
    locations = [ent.text for ent in parsed_doc.ents if ent.label_ in ["GPE", "LOC"]]

    for person in persons:
        for org in orgs:
            for loc in locations if locations else ["N/A"]:
                structured_info.append([person, org, loc])

df_full = pd.DataFrame(structured_info, columns=["Person", "Organization", "Location"])

print("\n========== Persons, Organizations & Locations ==========")
print(df_full)

# -----------------------------
# Step 6: Save results to CSV
# -----------------------------
df_entities.to_csv("named_entities.csv", index=False)
df_person_org.to_csv("person_organization.csv", index=False)
df_full.to_csv("person_org_location.csv", index=False)

print("\n✅ Results saved as CSV files")
