import unittest

import leet074_search_2d_matrix as search_2d_matrix


class Test074(unittest.TestCase):

    def test_search_2d_matrix(self):
        expected = [True, False]

        for entry, input in enumerate(search_2d_matrix.myinput):
            self.assertEqual(search_2d_matrix.leetSolve(
                input['matrix'], input['target']), expected[entry])

    def test_search_2d_matrix_clever(self):
        expected = [True, False]

        for entry, input in enumerate(search_2d_matrix.myinput):
            self.assertEqual(search_2d_matrix.leetSolveClever(
                input['matrix'], input['target']), expected[entry])
