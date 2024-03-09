# unittesting abc functions roots.py

import roots
from roots import abc
import doctest
import unittest

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(roots))
    return tests

class AbcTestCases(unittest.TestCase):
    def test_happy_path(self):
        """a, b, c params all integers, 2 solutions"""
        self.assertEqual(abc(1,5,6), [-2.0, -3.0])

    def test_happy_path_2(self):
        """a, b, c params all integers, 1 solution"""
        self.assertEqual(abc(1,2,1), [-1.0])

    def test_non_int(self):
        """a, b, c not only integers"""
        self.assertRaises(TypeError, abc, 1.5,5,6)

    def test_ais0(self):
        """a=0"""
        self.assertRaises(ValueError, abc, 0,5,6)



if __name__ == '__main__':
    unittest.main()