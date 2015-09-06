class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        if len(nums) == 0:
            return 0
        start = 0
        end   = len(nums) - 1
        while start < end:
            if nums[start] == val:
                temp        = nums[end]
                nums[end]   = nums[start]
                nums[start] = temp
                end = end - 1
            else:
                start = start + 1
        if nums[start] == val:
            return start
        else:
            return start + 1


sol = Solution()
arr = [1,1,2,3,5,3]
print("removed 3: {}".format(arr[:sol.removeElement(arr, 3)]))

arr = []
print("removed 5: {}".format(arr[:sol.removeElement(arr, 3)]))
