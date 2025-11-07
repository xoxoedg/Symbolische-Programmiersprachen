import re
import nltk
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize, TweetTokenizer
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
import nltk.data

# Modell Punkt: Realizes that the periods in Mrs. and Mr. are not sentence boundaries
nltk.download('punkt')
nltk.download('punkt_tab')

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
text = "Dr. Jones is the U.S. President's advisor."

sentences = sent_tokenize(text)
print("Sätze: ", sentences)

for s in sentences:
    print("Tokens:", word_tokenize(s))

text2 = "Mr. Green arrived. He met Mrs. Smith, who was waiting at 3 p.m."
sentences_2 = sent_tokenize(text2)

for s in sentences_2:
    print(word_tokenize(s))


#Tweet Tokenizer für Social Media

tokenizer = TweetTokenizer()

print(tokenizer.tokenize("LOL!!! Can't wait for #Friday 😂 @you"))
