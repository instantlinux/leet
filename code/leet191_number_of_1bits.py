"""number_of_1bits (191)

Write a function that takes an unsigned integer and returns the number
of '1' bits it has (also known as the Hamming weight).

Examples:
  Input: 11
  Output: 3
  Explanation: Integer 11 has binary representation
     00000000000000000000000000001011

  Input: 128
  Output: 1
  Explanation: Integer 128 has binary representation
     00000000000000000000000010000000
"""

myinput = [11, 128]


def leetSolve(num):
    """number_of_1bits algorithm

    Obvious way

    Args:
        num: arbitrary positive integer
    Returns:
        int:  number of bits set
    """
    count = 0
    while num > 0:
        count += num & 1
        num = num >> 1
    return count


for entry, input in enumerate(myinput):
    print "list %d: %s" % (entry + 1, leetSolve(input))
