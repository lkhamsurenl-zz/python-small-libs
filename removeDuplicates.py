class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        nonDup = 0
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[nonDup + 1] = nums[i + 1]
                nonDup = nonDup + 1
        return nonDup + 1 if len(nums) != 0 else 0


sol = Solution()
# empty
print("empty: {}".format(sol.removeDuplicates([])))

arr = [1,1,2]
length = sol.removeDuplicates(arr)
print("removed: {} of {}".format(arr, arr[:length]))


arr = [1,1,2, 2, 3,3,3]
length = sol.removeDuplicates(arr)
print("removed: {} of {}".format(arr, arr[:length]))


arr = [1,1,2, 2, 3,3,3,4]
length = sol.removeDuplicates(arr)
print("removed: {} of {}".format(arr, arr[:length]))
