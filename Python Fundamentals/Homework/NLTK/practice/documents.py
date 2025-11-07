import nltk
from nltk.corpus import brown, gutenberg
from nltk import Text
import matplotlib.pyplot as plt


print(brown.categories())

words = brown.words(categories="news")
print(words[:30])

print(brown.fileids()[:5])
print(brown.sents(fileids='ca01')[:2])

print(brown.readme())


print("----------------------")
# Text wrapper und der text wird zu einem intelligenten text
words = gutenberg.words("austen-emma.txt")
emma = Text(words)

emma.concordance("Emma")
emma.dispersion_plot(["Emma", "Harriet", "Knightley"])

plt.show()