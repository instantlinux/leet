"""minimum_window_sub (76)

Given a string S and a string T, find the minimum window in S which
will contain all the characters in T in complexity O(n).

Example:
  Input: S = "ADOBECODEBANC", T = "ABC"
  Output: "BANC"

Note:
  * If there is no such window in S that covers all characters in T,
    return the empty string "".

  * If there is such window, you are guaranteed that there will always
    be only one unique minimum window in S.

"""

myinput = [
    dict(s="ADOBECODEBANC", t="ABC")]


def leetSolve(s_haystack, t_hay):
    """Finds minimum window within haystack where hay can be found

    Obvious way

    Args:
        s_haystack (str): arbitrary string
        t_hay (str): string to match within haystack
    Returns:
        str:  shortest substring
    """
    match_map = {}
    for i in range(len(s_haystack)):
        match_map[t_hay.find(s_haystack[i])] = i

    """ TODO
    for i in range(len(s_haystack)):
        if matching[i]:
            for j in t_hay:
                # TODO
                continue
        for j in range(i + 1, len(items) + 1):
            sum = _sumRange(items, (i, j))
            maxResult = max(sum, maxResult)
    return maxResult
    """


for entry, input in enumerate(myinput):
    print "list %d: %s" % (entry + 1, leetSolve(input['s'], input['t']))
