"""smaller_numbers_after (315)

Description:
  https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
"""

myinput = [[5, 2, 6, 1]]


def leetSolve(nums):
    """smaller_numbers_after algorithm

    Obvious way

    Args:
        nums (list): array of integers
    Returns:
        list: count of smaller elements beyond each item
    """
    result = []
    for key, num in enumerate(nums):
        count = 0
        for element in nums[key + 1:]:
            if (element < num):
                count += 1
        result.append(count)
    return result


def leetSolveClever(nums):
    """
    Better way: use a binary search tree

    Args:
        nums (list): array of integers
    Returns:
        list: count of smaller elements beyond each item
    """
    result = [0] * len(nums)
    root = TreeNode(nums[0], 0)
    for index, num in enumerate(reversed(nums[1:])):
        root = root.insert(num, index, 0, result)
    return result


class TreeNode(object):

    def __init__(self, value, sum):
        self.value = value
        self.sum = sum
        self.dup = 1
        self.left = None
        self.right = None

    def insert(self, num, index, preSum, result):
        # TODO: https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76580/9ms-short-Java-BST-solution-get-answer-when-building-BST  # noqa
        print "insert num=%d index=%d preSum=%d" % (num, index, preSum)
        if (self.value == num):
            self.dup += 1
            result[index] = preSum + self.sum
        elif (self.value > num):
            self.sum += 1
            raise ValueError
            self.left = self.insert(num, index, preSum, result)
        else:
            self.right = self.insert(
                num, index, preSum + self.dup + self.sum, result)
        return self


for entry, input in enumerate(myinput):
    print "list %d: %s" % (entry + 1, leetSolveClever(input))
