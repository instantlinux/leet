import unittest

import leet257_binary_tree_paths as binary_tree_paths


class Test257(unittest.TestCase):

    def test_binary_tree_paths(self):
        expected = [
            ['1->2->5->3', '1->2->5->6->10->8', '1->2->5->6->10->13'],
            ['1000'],
            []]

        for entry, input in enumerate(binary_tree_paths.myinput):
            self.assertEqual(binary_tree_paths.leetSolve(input),
                             expected[entry])
