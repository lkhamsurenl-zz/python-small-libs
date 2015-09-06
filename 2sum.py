# Fund 2 indices such that the numbers add up to target
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        dic = {} # includes remaining value to adding to target
        for i in range(len(nums)):
            if nums[i] in dic:
                # we found the number in there
                return [dic[nums[i]], i]
            else:
                dic[target - nums[i]] = i
        return [] # if no such number exist


sol = Solution()
# multiple solutions
print sol.twoSum([1,2,3,4,5], 9)
