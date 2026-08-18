import spacy

nlp = spacy.load("en_core_web_sm")

text = """
Barack Obama visited India.

Spiderman visited New York.

Tony Stark works at Stark Industries.

Harry Potter studies at Hogwarts university.
"""

doc = nlp(text)

for entity in doc.ents:
    print(entity.text, "->", entity.label_)