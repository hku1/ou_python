# unit testen functie

import dictvaluesfromto
import doctest
import unittest

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(dictvaluesfromto))
    return tests

class Dictvalfrm2TestCases(unittest.TestCase):

    def test_happy_path(self):
        """two lists with the same number of itemsnmbrdict= {'a': 2, 'b': 4, 'c': 8.9}"""
        nmbrdict= {'a': 2, 'b': 4, 'c': 8.9}

        self.assertEqual(mymath.pairwise_sum(xs1, xs2), [7, 9, 11, 13, 15])
