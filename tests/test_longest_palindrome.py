import unittest

import leet409_longest_palindrome as longest_palindrome


class Test409(unittest.TestCase):

    def test_longest_palindrome(self):
        expected = [7]

        for entry, input in enumerate(longest_palindrome.myinput):
            self.assertEqual(longest_palindrome.leetSolve(input),
                             expected[entry])

    def test_longest_palindrome_clever(self):
        expected = [7]

        for entry, input in enumerate(longest_palindrome.myinput):
            self.assertEqual(longest_palindrome.leetSolveClever(input),
                             expected[entry])
