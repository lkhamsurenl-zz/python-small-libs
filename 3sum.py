import itertools
# find all triplets (in non-descending order) that adds up to 0
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        nums.sort()
        ans = []
        for i in range(len(nums)):
            # i is the smallest value
            j = i + 1
            k = len(nums) - 1
            while j < k:
                curr = nums[i] + nums[j] + nums[k]
                if curr == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j = j + 1
                    k = k - 1
                elif curr < 0:
                    j = j + 1
                else:
                    k = k - 1
        return list(k for ans, _ in itertools.groupby(ans))

sol = Solution()
# no solution
print("arr: {} sol: {}".format([1,2,3], sol.threeSum([1,2,3])))
# exactly one
print("arr: {} sol: {}".format([1,-4,3], sol.threeSum([1,-4,3])))
# 2 or more with shared value
print("sol [-1, 0, 1], [-2, 0, 2]. {}".format([1,0,-1,2, -2], sol.threeSum([1,2,-2,-1,0])))
# no duplicate
print("sol [-1, 0, 1]. {}".format([1,0,-1,1, -1], sol.threeSum([1,1,-1,-1,0])))
print("{}".format(sol.threeSum([0, 0, 0, 0])))
