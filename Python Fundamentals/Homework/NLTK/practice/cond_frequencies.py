from nltk.probability import ConditionalFreqDist, FreqDist
from nltk.tokenize import word_tokenize

sent = """
the the the dog dog some other words
that we do not care about
"""

cfdist = ConditionalFreqDist()

for word in word_tokenize(sent):
    condition = len(word)
    cfdist[condition][word] += 1

print(cfdist.__repr__())
print(cfdist[3].most_common())
print(cfdist.conditions())


ent = 'This is an example sentence'
fdist = FreqDist()
for word in word_tokenize(sent):
     fdist[word.lower()] += 1

