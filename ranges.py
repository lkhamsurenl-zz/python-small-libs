class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        return self.recRange(nums)
    def recRange(self, nums):
        ran = []
        if len(nums) <= 0:
            return ran
        low = 0
        high = 1
        while high < len(nums) and nums[high - 1] + 1 == nums[high]:
            high = high + 1
        # no longer in range
        if low != high -1:
            ran.append("{}->{}".format(nums[low], nums[high -1]))
        else:
            ran.append("{}".format(nums[low]))
        if high == len(nums):
            return ran
        else:
            # not done going over
            ran = ran + self.recRange(nums[high:])
        return ran

sol = Solution()
for ran in [[], [1,2], [1], [1,2,3,5,7], [1,2,3,5,6,7,8,9]]:
    print sol.summaryRanges(ran)
