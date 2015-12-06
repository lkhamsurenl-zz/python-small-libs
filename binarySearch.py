# Binary search in a array
class Solution:
    def binarySearch(self, nums, target):
        return self.binarySearchInRange(nums, 0, len(nums) -1, target)

    # return index of the target, -1 otherwise
    def binarySearchInRange(self, nums, low, high, target):
        if low > high:
            return -1
        mid = low + (high - low) / 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binarySearchInRange(nums, mid + 1, high, target)
        else:
            return self.binarySearchInRange(nums, low, mid -1, target)

    def binarySearchIndex(self, nums, target):
        return self.__binarySearchIndexRange__(nums, 0, len(nums) - 1, target)

    def __binarySearchIndexRange__(self, nums, low, high, target):
        if low > high:
            return low
        if low == high:
            return low if nums[low] > target else low + 1
        mid = (high - low) / 2 + low
        if nums[mid] < target < nums[mid + 1]:
            return mid + 1
        if nums[mid] <= target:
            return self.__binarySearchIndexRange__(nums, mid + 1, high, target)
        else:
            return self.__binarySearchIndexRange__(nums, low, mid - 1, target)

    ####################### Search with Repeated Elements ##################
    # find the lowest index of target in array
    def binarySearchInRangeLowestIndex(self, nums, low, high, target):
        if low >= high:
            return low if low == high and nums[high] == target else -1
        mid = low + (high - low) / 2
        if nums[mid] != target and nums[mid + 1] == target:
            return mid + 1
        elif nums[mid] >= target:
            return self.binarySearchInRangeLowestIndex(nums, low, mid, target)
        else:
            return self.binarySearchInRangeLowestIndex(nums, mid + 1, high, target)

        # find the highest index of target in array
    def binarySearchInRangeHighestIndex(self, nums, low, high, target):
        if low >= high:
            return high if low == high and nums[high] == target else -1
        mid = low + (high - low) / 2
        if nums[mid] == target and nums[mid + 1] != target:
            return mid
        elif nums[mid] > target:
            return self.binarySearchInRangeHighestIndex(nums, low, mid - 1, target)
        else:
            return self.binarySearchInRangeHighestIndex(nums, mid + 1, high, target)

    # find a range that spans target in nums
    def binarySearchRange(self, nums, target):
        low = self.binarySearchInRangeLowestIndex(nums, 0, len(nums) -1, target)
        high = self.binarySearchInRangeHighestIndex(nums, 0, len(nums) -1, target)
        return [low, high]

    #############################  Rotation ################################
    def findRotationIndex(self, nums):
        return self.findRotationIndexInRange(nums, 0, len(nums) - 1)

    # Helper function to find rotation index in sorted array
    def findRotationIndexInRange(self, nums, low, high):
        if low >= high:
            return low
        mid = low + (high - low) / 2
        if nums[mid] > nums[mid + 1]: # mid is climax
            return mid
        elif nums[low] <= nums[mid]:
            return self.findRotationIndexInRange(nums, mid + 1, high)
        else:
            return self.findRotationIndexInRange(nums, low, mid - 1)

    def searchInRotatedArray(self, nums, target):
        index = self.findRotationIndex(nums)
        first = self.binarySearchInRange(nums, 0, index, target)
        if first < 0:
            return self.binarySearchInRange(nums, index + 1, len(nums) - 1, target)
        else:
            return first
            
sol = Solution()
print("Testing binarySearch")
for (arr, target, want) in [ ([1,2,3,4,5], 3, 2), ([1,2,3], 5, -1), ([], 3, -1) ]:
    got = sol.binarySearch(arr, target)
    assert got == want, \
        "binarySearch({}, {}) = {}; want: {}".format(arr, target, got, want)

print("Testing findRotationIndex")
for (arr, want) in [ ([1,2,3,4,5], 4), ([2,3,1], 1), ([], 0), ([7,1,3,4], 0) ]:
    got = sol.findRotationIndex(arr), \
        "findRotationIndex({}) = {}; want: {}".format(arr, got, want)

print("Testing searchInRotatedArray")
for (arr, target, want) in [ ([1,2,3,4,5], 5, 4), ([1,2,3,4,5], 3, 2), ([1,2,3,4,5], 9, -1),\
                             ([4,5,1,2,3], 5, 1), ([4,5,1,2,3], 2, 3) ]:
    got = sol.searchInRotatedArray(arr, target)
    assert got == want, \
        "searchInRotatedArray({}, {}) = {}; want: {}".format(arr, target, got, want)

print("Testing binarySearchInRangeLowestIndex")
for (arr, target, want) in [ ([1,2,3,4,5], 5, 4), ([1,2,3,4,5], 3, 2), ([1,2,3,4,5], 9, -1),\
                             ([1,2,3,3,4,5], 3, 2), ([1,1,1], 1, 0), ([], 3, -1)]:
    got = sol.binarySearchInRangeLowestIndex(arr, 0, len(arr) - 1, target)
    assert got == want, \
        "binarySearchInRangeLowestIndex({}, {}, {}, {}) = {}; want: {}".format(arr,\
            0, len(arr) - 1, target, got, want)

print("Testing binarySearchInRangeHighestIndex")
for (arr, target, want) in [ ([1,2,3,4,5], 5, 4), ([1,2,3,4,5], 3, 2), ([1,2,3,4,5], 9, -1),\
                             ([1,2,3,3,4,5], 3, 3), ([1,1,1], 1, 2), ([], 3, -1)]:
    got = sol.binarySearchInRangeHighestIndex(arr, 0, len(arr) - 1, target)
    assert got == want, \
        "binarySearchInRangeHighestIndex({}, {}, {}, {}) = {}; want: {}".format(arr,\
            0, len(arr) - 1, target, got, want)

print("Testing binarySearchRange")
for (arr, target, want) in [ ([1,2,3,4,5], 5, [4,4]), ([1,2,3,4,5], 3, [2,2]),\
                            ([1,2,3,4,5], 9, [-1,-1]), ([1,2,3,3,3,4,5], 3, [2,4]),\
                            ([1,1,1], 1, [0,2]) ]:
    got = sol.binarySearchRange(arr, target)
    assert got == want, \
        "binarySearchRange({}, {}) = {}; want: {}".format(arr, target, got, want)

print("Testing binarySearchIndex")
for (arr, target, want) in [ ([1,2,3,4,5], 5, 5), ([1,4,5], 3, 1),\
                            ([], 9, 0), ([1,2,3,3,3,4,5], 6, 7), ([1,2,3], 2, 2) ]:
    got = sol.binarySearchIndex(arr, target)
    assert got == want, \
        "binarySearchRange({}, {}) = {}; want: {}".format(arr, target, got, want)

print("ALL TEST PASS!!!")
