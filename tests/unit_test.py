import unittest
import algorithims_test
import match_test



query = 'simple string'
choices = ['simple strings', 'strings are simple', 'sim string']

class TestStringMatch(unittest.TestCase):

    def test_trigram(self):
        self.assertEqual(algorithims_test.trigram("simple string", "simple strings"), 0.8, "Should be 0.8")

    def test_cosine(self):
        self.assertEqual(algorithims_test.cosine("simple string", "simple strings"), 0.4999999999999999, "Should be 0.4999999999999999")

    def test_levenshtein(self):
        self.assertEqual(algorithims_test.levenshtein("simple string", "simple strings"), 0.9285714285714286, "Should be 0.9285714285714286")

    def test_jaro_winkler(self):
        self.assertEqual(algorithims_test.jaro_winkler("simple string", "simple strings"), 0.847985347985348, "Should be 0.847985347985348")

    def test_extract(self):
        self.assertEqual(match_test.extract(query, choices), [('simple strings', 0.8), ('strings are simple', 0.631579), ('sim string', 0.642857)], "Should be [('simple strings', 0.8), ('strings are simple', 0.631579), ('sim string', 0.642857)]")    

    def test_extractOne(self):
        self.assertEqual(match_test.extractOne(query, choices), ('simple strings', 0.8), "Should be ('simple strings', 0.8)")    


if __name__ == "__main__":

    unittest.main()