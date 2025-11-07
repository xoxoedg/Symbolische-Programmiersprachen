import nltk


class LangModeler(object):
    def __init__(self, languages, words):
        self.languages = languages
        self.words = words

    def build_language_models(self):
        # TODO return ConditionalFrequencyDistribution of bigrams in the UDHR corpus conditioned on each language
        # hint: use nltk.ConditionalFreqDist
        pass

    def guess_language(self,language_model_cfd, text):
        """it should return a tuple (most_likely_language, confidence_score) for a
        given text according to the scores, where confidence_score rounded to two
        decimal places"""

        #TODO for each language calculate the overall score of a given text,
        # and return a tuple (most_likely_language, confidence_score)
        pass
