# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def toStr(self):
        return (self.start, self.end)

class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        lowIndex = self.smallestIntervalInRange(intervals, 0, len(intervals) - 1, newInterval)
        #print("low: {}".format(lowIndex))
        highIndex = self.biggestIntervalInRange(intervals, 0, len(intervals) - 1, newInterval)
        #print("high: {}".format(highIndex))
        mergedIntervals = []
        if lowIndex != 0:
            mergedIntervals = mergedIntervals + intervals[:lowIndex]
        newLow = min(intervals[lowIndex].start, newInterval.start) if len(intervals)>lowIndex >= 0 else newInterval.start
        newHigh =  max(intervals[highIndex].end, newInterval.end) if 0<=highIndex < len(intervals) else newInterval.end
        mergedIntervals = mergedIntervals + [Interval(newLow,newHigh)]
        if highIndex < len(intervals) - 1:
            mergedIntervals = mergedIntervals + intervals[highIndex + 1:]
        return mergedIntervals

    def smallestIntervalInRange(self, intervals, low, high, newInterval):
        if low > high:
            return low # NOTE: low can be len(intervals)
        mid = low + (high - low) / 2
        if intervals[mid].start == newInterval.start or (intervals[mid].start < newInterval.start and intervals[mid].end >= newInterval.start):
            return mid
        elif intervals[mid].start < newInterval.start:
            return self.smallestIntervalInRange(intervals, mid + 1, high, newInterval)
        else:
            return self.smallestIntervalInRange(intervals, low, mid - 1, newInterval)

    def biggestIntervalInRange(self, intervals, low, high, newInterval):
        if low > high:
            return high # NOTE: high can be less than 0
        mid = low + (high - low) / 2
        if intervals[mid].end == newInterval.end or (intervals[mid].end > newInterval.end and newInterval.end >= intervals[mid].start):
            return mid
        elif intervals[mid].end < newInterval.end:
            return self.biggestIntervalInRange(intervals, mid + 1, high, newInterval)
        else:
            return self.biggestIntervalInRange(intervals, low, mid - 1, newInterval)


sol = Solution()
intervals = [Interval(1,2), Interval(3,5),Interval(6,7),Interval(8,10),Interval(12, 16)]
newIntervals = sol.insert(intervals, Interval(4, 9))
for i in newIntervals:
    print("{} and {}".format(i.start, i.end))
###
print("with exact inclusion test:")
intervals = [Interval(1,2), Interval(3,5),Interval(6,7),Interval(8,10),Interval(12, 16)]
newInterval = Interval(5, 10)
newIntervals = sol.insert(intervals, newInterval)
ans = []
for i in newIntervals:
    ans.append((i.start, i.end))
print("{} after insert {} is: {}".format(map(lambda x: x.toStr(), intervals), newInterval.toStr(), ans))

###
print("no merging in the back:")
intervals = [Interval(1,2), Interval(3,5),Interval(6,7),Interval(8,10),Interval(12, 16)]
newInterval = Interval(20, 30)
newIntervals = sol.insert(intervals, newInterval)
ans = []
for i in newIntervals:
    ans.append((i.start, i.end))
print("{} after insert {} is: {}".format(map(lambda x: x.toStr(), intervals), newInterval.toStr(), ans))

###
print("no merging at the front:")
intervals = [Interval(1,2), Interval(3,5),Interval(6,7),Interval(8,10),Interval(12, 16)]
newInterval = Interval(-1, 0)
newIntervals = sol.insert(intervals, newInterval)
ans = []
for i in newIntervals:
    ans.append((i.start, i.end))
print("{} after insert {} is: {}".format(map(lambda x: x.toStr(), intervals), newInterval.toStr(), ans))
