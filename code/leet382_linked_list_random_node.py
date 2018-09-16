"""linked_list_random_node (382)

Description:
  See https://leetcode.com/problems/linked-list-random-node/description/
"""

import os
from lib.singly_linked_list import SinglyLinkedList

myinput = [
    [1, 2, 3],
    [50, 70, 90, 200, 30]]


def leetSolve(nums):
    """Return a random value within a list; assumes list length is
    within range of a 64-bit long int

    Obvious way

    Args:
        nums: integers to populate linked list
    Returns:
        int: arbitrary value in list
    """
    head = SinglyLinkedList(nums[0])
    head.load(nums[1:])

    len = head.length()
    rand = int(os.urandom(8).encode('hex'), 16) % len
    node = head
    for count in range(0, rand):
        node = node.next
    return node.val


def leetSolveClever(nums):
    """Return a random value within a list

    More-clever way: may be faster if the modulo operator isn't more
    costly than scanning the list 1.5 times (the above case has to
    scan it to count length, and then scan part of it to return a
    value). This requires only O(n) time to scan list once.

    Args:
        nums: integers to populate linked list
    Returns:
        int: arbitrary value in list
    """
    head = SinglyLinkedList(nums[0])
    head.load(nums[1:])

    result = head.val
    count = 2
    node = head.next
    rand = int(os.urandom(8).encode('hex'), 16)
    while (node):
        if (rand % count == 0):
            result = node.val
        count += 1
        node = node.next
    return result


for entry, input in enumerate(myinput):
    print "case %d: %s" % (entry + 1, leetSolveClever(input))
