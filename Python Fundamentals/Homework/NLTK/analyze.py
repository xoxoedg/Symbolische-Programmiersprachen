from nltk import FreqDist
from nltk import word_tokenize, sent_tokenize
import re

class Analyzer(object):
    def __init__(self, path):
        '''reads the file text, creates the list of words (use nltk.word_tokenize to tokenize the text),
            and calculates frequency distribution '''
        self.text = None #TODO the text from the file
        self.words = None #TODO the list of words from text file
        self.token_counts = None #TODO frequency distribution of words from text file
        pass

    def numberOfTokens(self):
        '''returns number of tokens in the text '''
        pass

    def numberOfSents(self):
        '''returns the number of sentences in the text'''
        pass

    def probDist(self):
        '''returns the probability distribution of tokens'''
        pass

    def topFiveFreqTokens(self):
        '''returns returns a list of strings of the top five most frequent tokens in the text
        (sorted by frequency from high to low and alphabetically in case of ties)'''
        pass

    def lexicalDiversity(self):
        '''returns the lexical diversity of the text '''
        pass

    def getYears(self):
        '''returns a list of strings that are four-digit numbers'''
        pass

    def numberOfHapaxes(self):
        '''returns the number of hapaxes in the text'''
        pass

    def avWordLength(self):
        '''calculate and return the average word length in the text, rounded to two decimal places'''
        pass

