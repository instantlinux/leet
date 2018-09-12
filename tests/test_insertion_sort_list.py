import unittest

import leet147_insertion_sort_list as insertion_sort_list


class Test147(unittest.TestCase):

    def test_insertion_sort_list(self):
        expected = [
            [1, 2, 3, 4],
            [-1, 0, 3, 4, 5],
            [],
            [1000]]

        for entry, input in enumerate(insertion_sort_list.myinput):
            self.assertEqual(insertion_sort_list.leetSolve(input),
                             expected[entry])

    def test_insertion_sort_list_inplace(self):
        expected = [
            [1, 2, 3, 4],
            [-1, 0, 3, 4, 5],
            [],
            [1000]]

        for entry, input in enumerate(insertion_sort_list.myinput):
            self.assertEqual(insertion_sort_list.leetSolveInPlace(
                input), expected[entry])
