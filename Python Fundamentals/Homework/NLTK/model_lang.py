from nltk import bigrams
from nltk.corpus import udhr
from nltk.probability import ConditionalFreqDist


class LangModeler(object):
    def __init__(self, languages, words):
        self.languages = languages
        self.words = words

    # def build_language_models(self):
    #     cfd: ConditionalFreqDist = ConditionalFreqDist()
    #     for language in self.languages:
    #         text = " ".join(self.words[language]).lower()
    #         text_biagram = list(bigrams(text))
    #         for c1, c2 in text_biagram:
    #             b_str = c1 + c2
    #             cfd[language][b_str] += 1
    #     return cfd

    def build_language_models(self):
        cfd: ConditionalFreqDist = ConditionalFreqDist()
        for language in self.languages:
            text_biagram = list(bigrams([word.lower() for word in self.words[language]]))
            for c1, c2 in text_biagram:
                b_str = c1 + c2
                cfd[language][b_str] += 1
        return cfd

    def guess_language(self, language_model_cfd, text):
        """it should return a tuple (most_likely_language, confidence_score) for a
        given text according to the scores, where confidence_score rounded to two
        decimal places"""

        # TODO for each language calculate the overall score of a given text,
        # and return a tuple (most_likely_language, confidence_score)
        pass


if __name__ == "__main__":
    print(udhr.fileids())
    languages = ['English', 'German_Deutsch', 'French_Francais']
    language_base = dict((language, udhr.words(language + '-Latin1')) for language in languages)
    print(language_base["English"])
    langModeler: LangModeler = LangModeler(languages, language_base)
    language_model_cfd: ConditionalFreqDist = langModeler.build_language_models()
    print(language_model_cfd.conditions())
    print(language_model_cfd["English"].N())
    print(language_model_cfd["English"]["th"])
