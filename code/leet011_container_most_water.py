"""container_most_water (11)

Given n non-negative integers a1, a2, ..., an , where each represents
a point at coordinate (i, ai). n vertical lines are drawn such that
the two endpoints of line i is at (i, ai) and (i, 0). Find two lines,
which together with x-axis forms a container, such that the container
contains the most water.

Note: You may not slant the container and n is at least 2.
* diagram *

The above vertical lines are represented by array
[1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue
section) the container can contain is 49.

Example:

  Input: [1,8,6,2,5,4,8,3,7]
  Output: 49

"""

myinput = [
    [1, 8, 6, 2, 5, 4, 8, 3, 7],
    [500, 10, 10, 5000, 501]]


def leetSolve(heights):
    """container_most_water algorithm

    Obvious way

    Returns:
        int: area between two height markers
    """
    area = 0
    for i, val1 in enumerate(heights):
        for j, val2 in enumerate(heights[i + 1:]):
            area = max(area, (j + 1 - i) * min(val1, val2))
            print '%d:%d/%d' % (i, j, area)
    return area


def leetSolveClever(heights):
    """container_most_water algorithm

    More-clever way

    Returns:
        int: area between two height markers
    """
    (upper, lower, area) = (len(heights) - 1, 0, 0)
    area = 0
    while lower < upper:
        area = max(area,
                   (upper - lower) * min(heights[lower], heights[upper]))
        if (heights[upper] < heights[lower]):
            upper -= 1
        else:
            lower += 1
    return area


for entry, x in enumerate(myinput):
    print "list %d: %s" % (entry + 1, leetSolve(x))
