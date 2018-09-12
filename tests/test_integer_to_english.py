import unittest

import leet273_integer_to_english as integer_to_english


class Test273(unittest.TestCase):

    def test_integer_to_english(self):
        expected = [
            "One Hundred Twenty Three",
            "Twelve Thousand Three Hundred Forty Five",
            ("One Million Two Hundred Thirty Four Thousand "
             "Five Hundred Sixty Seven"),
            ("One Billion Two Hundred Thirty Four Million Five Hundred "
             "Sixty Seven Thousand Eight Hundred Ninety One"),
            "Twenty Thousand",
            "Three Hundred Thousand",
            "Four Hundred Twelve Thousand Thirty One",
            "Zero"]

        for entry, input in enumerate(integer_to_english.myinput):
            self.assertEqual(integer_to_english.leetSolve(input),
                             expected[entry])
