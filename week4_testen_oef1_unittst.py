# unit testen functie

import dictvaluesfromto as dicval
import doctest
import unittest

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(dicval))
    return tests

class Dictvalfrm2TestCases(unittest.TestCase):

    def test_happy_path(self):
        """input dictionary with ints and/or floats, fromval, toval int or floats"""
        nmbrdict = {'a': 2, 'b': 4, 'c': 8.9}
        self.assertEqual(dicval.dictvaluesfromto(nmbrdict, 2, 16), {'a': 16, 'b': 4, 'c': 8.9})

    def test_nonmbrs(self):
        """input dictionary contains not only integers or floats"""
        nmbrdict = {'a': 2, 'b': 4, 'c': 'c'}
        self.assertRaises(TypeError, dicval.dictvaluesfromto, nmbrdict, 2, 16)


if __name__ == '__main__':
    unittest.main()