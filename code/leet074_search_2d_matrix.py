"""search_2d_matrix (292)

Description:
  See https://leetcode.com/problems/seach-a-2d-matrix/description/
"""

myinput = [
    dict(matrix=[[1, 3,  5, 7],
                 [10, 11, 16, 20],
                 [23, 30, 34, 50]],
         target=3),
    dict(matrix=[[10, 13,  25, 71],
                 [80, 101, 116, 203],
                 [1023, 1305, 3499, 5011]],
         target=3802)
]


def leetSolve(matrix, target):
    """Find target item in matrix

    Obvious way

    Args:
        matrix: 2D matrix, presorted left to right each row, with each row
                content than the previous
        target: object to locate
    Returns:
        bool: whether the target is present
    """

    for row in matrix:
        if (target > row[-1]):
            continue
        elif (target < row[0]):
            return False
        for item in row:
            if (target == item):
                return True
            elif (target < item):
                return False
    return False


def leetSolveClever(matrix, target):
    """Find target item in matrix

    Better way: binary-search

    Args:
        matrix: 2D matrix, presorted left to right each row
        target: object to locate
    Returns:
        bool: whether the target is present
    """

    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while (left <= right):
        mid = left + (right - left) // 2
        item = matrix[mid // cols][mid % cols]
        if (item < target):
            left = mid + 1
        elif (item > target):
            right = mid - 1
        else:
            return True
    return False


for entry, input in enumerate(myinput):
    print "case %d: %s" % (entry + 1, leetSolveClever(input['matrix'],
                                                      input['target']))
