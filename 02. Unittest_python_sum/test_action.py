# import unitest
# nazwa pliku test_toco chce testować
import unittest

import action  # import py file


# tworze klase i tworze unitest
class TestAction(unittest.TestCase):
    def test_suma(self):  # argumentem jest self

        self.assertEqual(action.suma(30, 5), 34)  # sprawdzam czy wynik jest to co chce
        self.assertEqual(action.suma(30, 7), 37)
        self.assertEqual(action.suma(30, 3), 33)
        self.assertEqual(action.suma(30, 8), 38)

# w shell piszę python -m unittest test_action.py