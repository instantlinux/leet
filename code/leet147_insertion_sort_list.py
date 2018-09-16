"""insertion_sort_list (147)

Description:
  See https://leetcode.com/problems/insertion-sort-list/description
"""

from lib.doubly_linked_list import DoublyLinkedList

myinput = [
    [4, 2, 1, 3],
    [-1, 5, 3, 4, 0],
    [],
    [1000]]


def leetSolve(nums):
    """Sort a list

    Obvious way

    Args:
        nums (list): integer list
    Returns:
        list: sorted list
    """
    result = DoublyLinkedList()
    for num in nums:
        result.insertSorted(num)
    return result.get()


def leetSolveInPlace(nums):
    """Sort a list

    The proper way as explicitly instructed in this Leet example ("sort in
    place"); not sure if it's very efficient vs inserting each item into
    a growing list that starts out empty as above.

    Args:
        nums (list): integer list
    Returns:
        list: sorted list
    """
    result = DoublyLinkedList()

    # Convert input to doubly-linked list
    for num in nums:
        result.append(num)

    result.sortInPlace()
    return result.get()


for entry, input in enumerate(myinput):
    print "case %d: %s" % (entry + 1, leetSolveInPlace(input))
