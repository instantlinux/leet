import unittest

import leet011_container_most_water as container_most_water


class Test011(unittest.TestCase):

    def test_container_most_water(self):
        expected = [49, 2000]
        for entry, input in enumerate(container_most_water.myinput):
            self.assertEqual(container_most_water.leetSolve(input),
                             expected[entry])

    def test_container_most_water_clever(self):
        expected = [49, 2000]
        for entry, input in enumerate(container_most_water.myinput):
            self.assertEqual(container_most_water.leetSolveClever(input),
                             expected[entry])
