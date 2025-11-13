from unittest import TestCase
# depending on whether your model_lang.py script is found within the same folder with
# this script and whether you have defined the src folder as the Source Root in PyCharm, you
# might need to change the following import to remove hw04_nltk

import nltk

from Homework.NLTK.model_lang import LangModeler

nltk.download('udhr')
from nltk.corpus import udhr


class LangGuesserTest(TestCase):

    def setUp(self):
        languages = ['English', 'German_Deutsch', 'French_Francais']

        # udhr corpus contains the Universal Declaration of Human Rights in over 300 languages
        language_base = dict((language, udhr.words(language + '-Latin1')) for language in languages)

        # build the language models
        self.langModeler = LangModeler(languages, language_base)

    def test_01_build_language_models(self):
        language_model_cfd = self.langModeler.build_language_models()
        bigrams = [('education', 'shall'), ('care', 'and'), ('no', 'one'), ("the", "law"), ("penal", "offence"), ("universal", "declaration")]
        some_word_counts_inEnglish = [language_model_cfd['English'][w] for w in bigrams]
        self.assertEqual(some_word_counts_inEnglish, [5, 2, 8, 4, 4, 2])

    def test_02_guess_language(self):

        text1 = "All humans are entitled to equal protection"
        text2 = "les êtres humains ont le droit à la liberté"
        text3 = "Gerechtigkeit und Frieden ist das höchste Streben"
        text4 = "Peter had been to the office before they arrived."
        text5 = "Es gibt viele wunderbare Orte in der Welt."

        language_model_cfd = self.langModeler.build_language_models()

        self.assertEqual(self.langModeler.guess_language(language_model_cfd, text1)[0], 'English')
        self.assertEqual(self.langModeler.guess_language(language_model_cfd, text2)[0], 'French_Francais')
        self.assertEqual(self.langModeler.guess_language(language_model_cfd, text3)[0], 'German_Deutsch')
        self.assertEqual(self.langModeler.guess_language(language_model_cfd, text4)[0], 'English')
        self.assertEqual(self.langModeler.guess_language(language_model_cfd, text5)[0], 'German_Deutsch')

        self.assertEqual(self.langModeler.guess_language(language_model_cfd, text1)[1], 0.01)
        self.assertEqual(self.langModeler.guess_language(language_model_cfd, text2)[1], 0.03)
        self.assertEqual(self.langModeler.guess_language(language_model_cfd, text3)[1], 0.00)

