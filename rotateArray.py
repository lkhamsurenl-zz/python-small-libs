class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        full = self.flip(nums, 0, len(nums) -1 )
        # then rotate at k
        return self.flip(self.flip(full, 0, k -1 ), k, len(nums) -1 )

    # helper funciton to reverse the array in 2 sections using index
    def flip(self, arr, low, high):
        while low < high:
            temp = arr[low]
            arr[low] = arr[high]
            arr[high] = temp
            low = low + 1
            high = high - 1
        return arr


sol = Solution()
arr = [1 ,2 ,3, 4, 5]
for k in range(1, len(arr)):
    print("rotation of {} in {}: {}".format(k , arr, sol.rotate(arr, k)))
