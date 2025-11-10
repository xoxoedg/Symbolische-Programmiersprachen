from locale import normalize

from nltk import FreqDist, bigrams
from nltk import word_tokenize, sent_tokenize
from typing import List
import re
from Homework.NLTK.document import TextDocument


class Analyzer(object):
    FILENAME = "ada_lovelace.txt"
    def __init__(self, path):

        '''reads the file text, creates the list of words (use nltk.word_tokenize to tokenize the text),
            and calculates frequency distribution '''
        self.text = TextDocument.from_file(Analyzer.FILENAME).text
        self.words = word_tokenize(self.text)
        self.token_counts = FreqDist(self.words)
        pass

    def numberOfTokens(self):
        return len(self.words)

    def numberOfSents(self):
        return sent_tokenize(self.text, "english")

    def probDist(self):
        return {word: self.token_counts.freq(word) for word in self.token_counts}

    def topFiveFreqTokens(self):
        return self.token_counts.most_common(5)

    def lexicalDiversity(self):
        return len(set(self.text))/len(self.text)

    def getYears(self):
        return [year for year in self.words if re.search("^[0-9]{3,4}$", year)]

    def numberOfHapaxes(self):
        return self.token_counts.hapaxes()

    def avWordLength(self):
        sum(len(w) for w in self.normalize()) / len(self.normalize())

    def normalize(self):
        return [re.sub(r"\W+", "", word.lower) for word in self.words if re.sub("\W+", "", word)]




if __name__ == "__main__":
    analyzer = Analyzer("./ada_lovelace.txt")
    print(analyzer.getYears())
    print(len(analyzer.text))
    print(analyzer.lexicalDiversity())
    print(analyzer.words)
    print(analyzer.token_counts)

    a = {"name": "yasin",
         "age": 15}

    print("------------------")

    print(analyzer.token_counts.most_common(5))
    print(sorted(analyzer.token_counts.most_common(5), key=lambda x:(-x[1], x[0])))

    print("------------------")
    print(type(a.items()))
    token_counts = analyzer.token_counts.items()
    var = {word: count / len(analyzer.words) for word, count in token_counts}
    print(var)
    for i, j in a.items():
        print(i, j)

    for i in a:
        print(i)