"""pascals_triangle (118)

Given a non-negative integer numRows, generate the first numRows of
Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers
directly above it.

Example:
  Input: 5
  Output:
  [
       [1],
      [1,1],
     [1,2,1],
    [1,3,3,1],
   [1,4,6,4,1]
  ]

"""

myinput = [5, 7]


def leetSolve(num):
    """pascals_triangle algorithm

    Obvious way

    Returns:
        list:  list of lists as defined
    """
    print num
    output = [[1]]
    for row in range(num):
        prev = [0] + output[row] + [0]
        output.append([prev[item] + prev[item + 1]
                       for item in range(row + 1)])
    return output[1:]


for entry, input in enumerate(myinput):
    print "list %d: %s" % (entry + 1, leetSolve(input))
