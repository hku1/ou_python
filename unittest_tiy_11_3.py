import unittest
from tiy_11_3_class import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        """
        Create employ instance

        """
        self.e = Employee('Harmjan', 'Kuipers', 90000)
    def test_default_raise(self):
        self.e.give_raise()
        self.assertEqual(self.e.salary, 95000)  # add assertion here

    def test_custom_raise(self):
        self.e.give_raise(10000)
        self.assertEqual(self.e.salary, 100000)  # add assertion here


if __name__ == '__main__':
    unittest.main()
