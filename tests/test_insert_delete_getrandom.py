import unittest

import leet380_insert_delete_getrandom as insert_delete_getrandom


class Test380(unittest.TestCase):

    def test_insert_delete_getrandom(self):
        expected = [2]

        for entry, input in enumerate(insert_delete_getrandom.myinput):
            self.assertEqual(insert_delete_getrandom.leetSolve(
                input), expected[entry])
