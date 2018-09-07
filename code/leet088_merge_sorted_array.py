"""merge_sorted_array (88)

Given two sorted integer arrays nums1 and nums2, merge nums2 into
nums1 as one sorted array.

Note:
* The number of elements initialized in nums1 and nums2 are m and n
  respectively.
* You may assume that nums1 has enough space (size that is greater or
  equal to m + n) to hold additional elements from nums2.

Example:

  Input:
  nums1 = [1,2,3,0,0,0], m = 3
  nums2 = [2,5,6],       n = 3

  Output: [1,2,2,3,5,6]

"""

myinput = [dict(nums1=[1, 2, 3, 0, 0, 0], nums2=[2, 5, 6], m=3, n=3)]


def leetSolve(nums1, nums2, m, n):
    """merge_sorted_array algorithm

    Obvious way

    Args:
        nums1 (list): sorted integer array long enough to hold nums2
        nums2 (list): sorted integer array
        m (int): number of significant values in nums1
        n (int): number of significant values in nums2
    Returns:
        list: original nums1 list with nums2 merged
    """
    ptr1, ptr2, pos = (m - 1, n - 1, len(nums1))
    while pos > 0:
        pos -= 1
        if (ptr1 >= 0 and nums1[ptr1] > nums2[ptr2]):
            nums1[pos] = nums1[ptr1]
            ptr1 -= 1
        else:
            nums1[pos] = nums2[ptr2]
            ptr2 -= 1
            if ptr2 < 0:
                break
    return nums1


for entry, input in enumerate(myinput):
    print "list %d: %s" % (entry + 1, leetSolve(
        input['nums1'], input['nums2'], input['m'], input['n']))
