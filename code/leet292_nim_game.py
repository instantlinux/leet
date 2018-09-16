"""nim_game (292)

Description:
  See https://leetcode.com/problems/nim-game/description/
"""

myinput = [4, 5, 8, 31, 32]


def leetSolve(num):
    """If opponent can win, we lose

    Obvious way

    Args:
        num: number of stones in pile
    Returns:
        bool: whether the game is winnable against opponent
    """

    result = True
    removeone = removetwo = removethree = True
    for stones in range(4, num + 1):
        result = not (removeone and removetwo and removethree)
        removeone = removetwo
        removetwo = removethree
        removethree = result
    return result

    # Note: the obvious optimization is to test for nonzero mod-4;
    #  i.e. return num % 4 but the above shows more clearly why
    #  the first-mover should never leave a number divisable by 4


for entry, input in enumerate(myinput):
    print "case %d: %s" % (entry + 1, leetSolve(input))
