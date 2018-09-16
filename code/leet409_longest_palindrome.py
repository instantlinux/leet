"""longest_palindrome (409)

Description:
  See https://leetcode.com/problems/longest-palindrome/description/
"""

myinput = ["abccccdd"]


def leetSolve(string):
    """Find longest palindrome the input letters can make

    Obvious way

    Args:
        string (str): case-sensitive string
    Returns:
        int: longest palindrome that can be made
    """

    contents = {}
    for byte in list(string):
        if (byte in contents):
            contents[byte] += 1
        else:
            contents[byte] = 1
    oddFound = 0
    longest = 0
    for val in contents.itervalues():
        longest += val & ~1
        if (val & 1 and not oddFound):
            oddFound = 1
    return longest + oddFound


def leetSolveClever(string):
    """Find longest palindrome the input letters can make

    Better way: count instances of where number of letters is odd

    Args:
        string (str): case-sensitive string
    Returns:
        int: longest palindrome that can be made
    """

    contents = {}
    for byte in list(string):
        if (byte in contents):
            contents[byte] = (contents[byte] + 1) & 1
        else:
            contents[byte] = 1
    oddsFound = 0
    for val in contents.itervalues():
        if (val % 2):
            oddsFound += 1
    return len(string) - oddsFound + min(oddsFound, 1)


for entry, input in enumerate(myinput):
    print "case %d: %s" % (entry + 1, leetSolveClever(input))
