# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        # sort intervals
        # invariant: no interval considering should marge previous ones
        intervals.sort(key = lambda x: x.start, reverse = False)
        mergedList = []
        for interval in intervals:
            if len(mergedList) == 0 or mergedList[-1].end < interval.start:
                mergedList.append(interval)
            # the only interval the current one can merge is the last in merg
            elif len(mergedList) !=0 and mergedList[-1].end >= interval.end:
                continue
            else:
                lastInterval = mergedList[-1]
                newInterval = Interval(lastInterval.start, interval.end)
                mergedList[-1] = newInterval # replace last interval
        return mergedList
sol = Solution()
# simple
intervals = [Interval(1,5), Interval(2,3),  Interval(4,7), Interval(8, 10), Interval(5,11)]
newList = sol.merge(intervals)
for i in newList:
    print("{} and {}".format(i.start, i.end))

print("More Test:")
intervals = [Interval(1,3), Interval(2,6), Interval(8,10), Interval(15,18)]
newList = sol.merge(intervals)
for i in newList:
    print("{} and {}".format(i.start, i.end))

print("Case of exact match")
intervals = [Interval(1,3), Interval(3,6), Interval(8,10), Interval(7,8)]
newList = sol.merge(intervals)
for i in newList:
    print("{} and {}".format(i.start, i.end))
