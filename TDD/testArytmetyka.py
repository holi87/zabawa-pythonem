from liczby import *
import unittest


class TestArytmetyka(unittest.TestCase):
    def testDodawanie(self):
        self.assertEqual(5, dodawanie(3, 2))
        self.assertEqual(33, dodawanie(36, -3))

    def testMnozenie(self):
        self.assertEqual(0, mnozenie(0, 1))

    def testDzielenie(self):
        self.assertEqual(2, dzielenie(4, 2))
        self.assertEqual("nie dziel przez zero", dzielenie(3, 0))

if __name__ == '__main__':
    unittest.main()
