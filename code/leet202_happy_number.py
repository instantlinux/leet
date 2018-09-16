"""happy_number (57)

Description:
  See https://leetcode.com/problems/happy-number/description/
"""

myinput = [19, 12345, 8432481, 3234568230]


def leetSolve(num, seen=[]):
    """happy_number algorithm

    Obvious way

    Args:
        num: candidate number
        seen: list of items seen, to detect cycles
    Returns:
        boolean: true if converged down to 1
    """
    result = 0
    for val in list(str(num)):
        result += int(val) * int(val)
    if (result == 1):
        return True
    elif (result in seen):
        return False
    return leetSolve(result, seen=seen + [result])


def leetSolveClever(num):
    """Floyd Cycle detection algorithm

    Args:
        num: candidate number
    Returns:
        boolean: true if converged down to 1
    """
    def sumDigitsSquared(num):
        result = 0
        for val in list(str(num)):
            result += int(val) * int(val)
        return result

    tortoise = hare = num
    while True:
        tortoise = sumDigitsSquared(tortoise)
        hare = sumDigitsSquared(hare)
        hare = sumDigitsSquared(hare)
        if (hare == tortoise):
            break
    return True if tortoise == 1 else False


for entry, input in enumerate(myinput):
    print "case %d: %s" % (entry + 1, leetSolveClever(input))
