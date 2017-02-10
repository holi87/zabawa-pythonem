from liczby import *
import unittest


class TestArytmetyka(unittest.TestCase):
    def testDodawanie(self):
        self.assertEqual(5, dodawanie(3, 2))

    def testDodawanieZUjemna(self):
        self.assertEqual(33, dodawanie(36, -3))

    def testMnozenie(self):
        self.assertEqual(0, mnozenie(0, 1))

    def testDzielenie(self):
        self.assertEqual(2, dzielenie(4, 2))

    def testCzyDzielenieZwracaNoneTylkoGdyDzieliPrzezZero(self):
        self.assertIsNotNone(dzielenie(1, 3))
        self.assertIsNone(dzielenie(1, 0))

if __name__ == '__main__':
    unittest.main()
