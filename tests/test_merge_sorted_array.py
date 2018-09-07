import unittest

import leet088_merge_sorted_array as merge_sorted_array


class Test088(unittest.TestCase):

    def test_merge_sorted_array(self):
        input = dict(nums1=[1, 2, 3, 0, 0, 0], nums2=[2, 5, 6], m=3, n=3)
        expected = [1, 2, 2, 3, 5, 6]

        self.assertEqual(merge_sorted_array.leetSolve(
            input['nums1'], input['nums2'], input['m'], input['n']), expected)
