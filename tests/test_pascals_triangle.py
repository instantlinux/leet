import unittest

import leet118_pascals_triangle as pascals_triangle


class Test118(unittest.TestCase):

    def test_pascals_triangle(self):
        expected = [
            [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]],
            [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1],
             [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1]]]

        for entry, input in enumerate(pascals_triangle.myinput):
            self.assertEqual(pascals_triangle.leetSolve(input),
                                                        expected[entry])
