"""insert_delete_getrandom (315)

Description:
  https://leetcode.com/problems/insert-delete-getrandom-o1/description/
"""

import os

myinput = [[1, 2]]


def leetSolve(nums):
    """insert_delete_getrandom algorithm

    Obvious way

    Args:
        nums (list): array of integers
    Returns:
        list: count of smaller elements beyond each item
    """
    randomSet = RandomizedSet()
    randomSet.insert(nums[0])
    randomSet.remove(nums[1])
    randomSet.insert(nums[1])
    randomSet.remove(nums[0])
    return randomSet.getRandom()


class RandomizedSet(object):
    def __init__(self):
        self.root = {}

    def insert(self, val):
        self.root[val] = None

    def remove(self, val):
        """Remove an item

        Args:
            val (int): item to be removed
        Returns:
            bool: True if item was present
        """
        try:
            del(self.root[val])
            return True
        except KeyError:
            return False

    def getRandom(self):
        rand = int(os.urandom(8).encode('hex'), 16)
        count = 1
        result = None
        for item in self.root.iterkeys():
            if (rand % count == 0 or result is None):
                result = item
            count += 1
        return result


for entry, input in enumerate(myinput):
    print "list %d: %s" % (entry + 1, leetSolve(input))
