"""insert_interval (57)

Given a set of non-overlapping intervals, insert a new interval into
the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to
their start times.

Examples:

  Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
  Output: [[1,5],[6,9]]

  Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
  Output: [[1,2],[3,10],[12,16]]
  Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

"""

myinput = [
    dict(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]),
    dict(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
         newInterval=[4, 8])]


def leetSolve(intervals, newInterval):
    """insert_interval algorithm

    Obvious way

    Returns:
        list: revised list of intervals
    """
    result = []
    start = intervals[0][0]
    for item in intervals:
        start = min(start, item[0])
        end = item[1]
        if (newInterval[0] <= end):
            # TODO
            continue
        else:
            result.append(item)
    return result


for entry, input in enumerate(myinput):
    print "list %d: %s" % (entry + 1, leetSolve(input['intervals'],
                                                input['newInterval']))
