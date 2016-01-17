class Solution:
    # @param num, a list of integer
    # @return nothing (void), do not return anything, modify num in-place instead.
    def nextPermutation(self, num):
        # find the index, in which everything is in descending order after that point
        index = self.findDescend(num)
        # reverse digits (index, len - 1)
        low = index
        high = len(num) - 1
        while low < high:
            temp = num[low]
            num[low] = num[high]
            num[high] = temp
            low = low + 1
            high = high - 1
        # if index == 0, then directly return since it's already done
        if index == 0:
            return num
        # find the place for index -1 to be in the sorted part (index, len - 1)
        placeInd = self.findInd(num, index)
        # next permutation is exactly when you switch the next big number to num[index -1 ]
        temp = num[index -1]
        num[index -1 ] = num[placeInd]
        num[placeInd] = temp
        return num

    def findDescend(self, num):
        lastDes = 0
        for i in range(1, len(num)):
            if num[i - 1] < num[i]:
                lastDes = i
        return lastDes
        
    def findInd(self, num, index):
        placeInd = index
        while placeInd < len(num):
            if num[index - 1] >= num[placeInd]:
                placeInd  = placeInd + 1
            else:
                break
        return placeInd

sol = Solution()
for arr in [[1 , 3, 2], [3, 2, 1], [5, 34, 4, 2, 1]]:
    print("next permutation of {} is: {}".format(arr, sol.nextPermutation(arr)))
