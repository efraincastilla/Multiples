import unittest
from multiples import Multiples

class TestMultiples(unittest.TestCase):

    def test_no_multiples_number(self):
        self.assertEqual(Multiples(7), "7")
        self.assertEqual(Multiples(4), "4")
        self.assertEqual(Multiples(8), "8")
		
    def test_multiple_of_3_number(self):
        self.assertEqual(Multiples(3), "Linio")
        self.assertEqual(Multiples(6), "Linio")
        self.assertEqual(Multiples(9), "Linio")

    def test_multiple_of_5_number(self):
        self.assertEqual(Multiples(5), "IT")
        self.assertEqual(Multiples(20), "IT")
        self.assertEqual(Multiples(25), "IT")
        self.assertEqual(Multiples(100), "IT")

    def test_multiple_of_3_and_5(self):
        self.assertEqual(Multiples(15), "Linianos")
        self.assertEqual(Multiples(30), "Linianos")
		
if __name__ == '__main__':
	unittest.main()