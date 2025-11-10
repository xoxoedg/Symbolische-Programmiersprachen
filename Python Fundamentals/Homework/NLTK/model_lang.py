import nltk
from nltk import bigrams
from nltk.corpus import udhr2
from nltk.probability import ConditionalFreqDist, FreqDist
from nltk.corpus import udhr

class LangModeler(object):
    def __init__(self, languages, words):
        self.languages = languages
        self.words = words

    def build_language_models(self):
        cfd = ConditionalFreqDist()
        for language in self.languages:
            text = self.words[language]
            bigramList = bigrams(text)
            for biagram in bigramList:
                biagram_as_string = "".join(biagram)
                cfd[language][biagram_as_string] = FreqDist(biagram_as_string)
        return cfd

    def guess_language(self,language_model_cfd, text):
        """it should return a tuple (most_likely_language, confidence_score) for a
        given text according to the scores, where confidence_score rounded to two
        decimal places"""

        #TODO for each language calculate the overall score of a given text,
        # and return a tuple (most_likely_language, confidence_score)
        pass


if __name__ == "__main__":
    print(udhr.fileids())
    languages = ['English','German_Deutsch','French_Francais']
    language_base = dict((language, udhr.words(language + '-Latin1')) for language in languages)
    langModeler = LangModeler(languages, language_base)
    language_model_cfd = langModeler.build_language_models()