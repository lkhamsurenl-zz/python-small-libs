# Write a function to change given array to a < b > c < d ...
class Solution:
    def alter(self, arr):
        if len(arr) <= 1:
            return arr
        if arr[0] > arr[1]:
            temp = arr[1]
            arr[1] = arr[0]
            arr[0] = temp
        for i in range(0, len(arr) - 2):
            # ascending or descending
            if arr[i] < arr[i + 1] < arr[i + 2] or arr[i] > arr[i + 1] > arr[i + 2]:
                temp = arr[i + 2]
                arr[i + 2] = arr[i + 1]
                arr[i + 1] = temp
        return arr

sol = Solution()
print sol.alter([6, 5, 4, 3, 2 , 1])
print sol.alter([1, 2])
print sol.alter([2 , 1])
print sol.alter([1 , 2 ,3 ,4])
print sol.alter([6, 5, 4, 3, 2 , 1][::-1])
print sol.alter([i for i in range(100)][::-1]) # large example
