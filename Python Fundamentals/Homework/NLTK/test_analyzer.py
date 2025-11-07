import os
from unittest import TestCase
# depending on whether your analyze.py script is found within the same folder with
# this script and whether you have defined the src folder as the Source Root in PyCharm, you
# might need to change the following import to remove hw04_nltk
from src.hw04_nltk.analyze import Analyzer
from nltk import FreqDist

class AnalyzerTest(TestCase):

  def setUp(self):
    # make sure that the path to the folder data corresponds the path in your computer
    path = os.path.join(os.path.dirname(__file__), "ada_lovelace.txt")
    self.analyzer = Analyzer(path)

  def constructor(self):
    self.assertEqual(type(self.analyzer.token_counts), FreqDist)

  def test_01_numberOfTokens(self):
    self.assertEqual(self.analyzer.numberOfTokens(), 4506)

  def test_03_numberOfSents(self):
    self.assertEqual(self.analyzer.numberOfSents(), 174)

  def test_02_probDist(self):
    self.assertEqual(len(self.analyzer.probDist()), 1390)
    self.assertAlmostEqual(self.analyzer.probDist()['Ada'], 0.0175322, 7)
    self.assertAlmostEqual(self.analyzer.probDist()['Mary'], 0.0008878, 7)

  def test_03_top5tokens(self):
    self.assertEqual(self.analyzer.topFiveFreqTokens(),[',', '.', 'the', 'of', 'her'])


  def test_04_diversity(self):
    self.assertEqual(round(self.analyzer.lexicalDiversity(), 4), 0.3085)

  def test_05_getYears(self):
    self.assertIn("1815", self.analyzer.getYears())
    self.assertIn("2005", self.analyzer.getYears())
    self.assertIn("1822", self.analyzer.getYears())

  def test_06_numberOfHapaxes(self):
    self.assertEqual(self.analyzer.numberOfHapaxes(),936)

  def test_07_avWordLength(self):
    avg_length = self.analyzer.avWordLength()
    self.assertIsInstance(avg_length, float)
    self.assertEqual(4.49, avg_length)
