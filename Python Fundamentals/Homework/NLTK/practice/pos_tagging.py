import nltk
import tkinter
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree

text = "Barack Obama was born in Hawaii and served as the 44th President of the United States."

#1 POS-Tagging & Named-Entity-Chunking
chunked = ne_chunk(pos_tag(word_tokenize(text)))

#2 Entitäten extrahieren
entities = []
for subtree in chunked:
    if isinstance(subtree, Tree):  # Tree = erkannte Entität
        label = subtree.label()    # z.B. PERSON, GPE, ORGANIZATION
        entity = " ".join(token for token, pos in subtree.leaves())
        entities.append({"entity": entity, "type": label})

#3 Ergebnis anzeigen
print(entities)