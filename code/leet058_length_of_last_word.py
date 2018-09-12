"""length_of_last_word (058)

Given a string s consists of upper/lower-case alphabets and empty
space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space
characters only.

Example:
  Input: "Hello World"
  Output: 5
"""

myinput = ["Hello World",
           "My movie phrase is supercalifragilisticexpialidocious ",
           "  \t\n"]


def leetSolve(phrase):
    """length_of_last_word algorithm

    Obvious way

    Args:
        phrase (str): a string of words
    Returns:
        int:  length of last word
    """

    count = 0
    whitespace_bytes = ' \t\n'
    chomping = True
    for ch in reversed(phrase):
        if (ch in whitespace_bytes):
            if (chomping):
                continue
            else:
                break
        chomping = False
        count += 1
    return count


for entry, input in enumerate(myinput):
    print "list %d: %s" % (entry + 1, leetSolve(input))
