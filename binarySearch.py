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
print("__________________________________________________________________")
print("Testing binarySearch")
assert(2 == sol.binarySearch([1,2,3,4,5], 3))
assert(-1 == sol.binarySearch([1,2,3], 5))
print("All test succeeded!")


print("__________________________________________________________________")
print("Testing findRotationIndex")
assert(4 == sol.findRotationIndex([1,2,3,4,5]))
assert(1 == sol.findRotationIndex([2, 3, 1]))
assert(0 == sol.findRotationIndex([]))
assert(0 == sol.findRotationIndex([7, 1, 3, 4]))
print("All test succeeded!")


print("__________________________________________________________________")
print("Testing searchInRotatedArray")
assert(4 == sol.searchInRotatedArray([1,2,3,4,5], 5))
assert(2 == sol.searchInRotatedArray([1,2,3,4,5], 3))
assert(-1 == sol.searchInRotatedArray([1,2,3,4,5], 9))
assert(1 == sol.searchInRotatedArray([4, 5, 1,2,3], 5))
assert(3 == sol.searchInRotatedArray([4, 5, 1,2,3], 2))
print("All test succeeded!")
print("__________________________________________________________________")

print("Testing binarySearchInRangeLowestIndex")
assert(4 == sol.binarySearchInRangeLowestIndex([1,2,3,4,5], 0, 4, 5))
assert(2 == sol.binarySearchInRangeLowestIndex([1,2,3,4,5], 0, 4, 3))
assert(-1 == sol.binarySearchInRangeLowestIndex([1,2,3,4,5], 0, 4, 9))
assert(2 == sol.binarySearchInRangeLowestIndex([1,2,3,3,3,4,5], 0, 6, 3))
assert(0 == sol.binarySearchInRangeLowestIndex([1,1,1], 0, 2, 1))
print("All test succeeded!")
print("__________________________________________________________________")

print("Testing binarySearchInRangeHighestIndex")
assert(4 == sol.binarySearchInRangeHighestIndex([1,2,3,4,5], 0, 4, 5))
assert(2 == sol.binarySearchInRangeHighestIndex([1,2,3,4,5], 0, 4, 3))
assert(-1 == sol.binarySearchInRangeHighestIndex([1,2,3,4,5], 0, 4, 9))
assert(4 == sol.binarySearchInRangeHighestIndex([1,2,3,3,3,4,5], 0, 6, 3))
assert(2 == sol.binarySearchInRangeHighestIndex([1,1,1], 0, 2, 1))
assert(4 == sol.binarySearchInRangeHighestIndex([5, 7, 7, 8, 8, 10], 0, 5, 8))
print("All test succeeded!")
print("__________________________________________________________________")

print("Testing binarySearchRange")
assert([4,4] == sol.binarySearchRange([1,2,3,4,5], 5))
assert([2,2] == sol.binarySearchRange([1,2,3,4,5], 3))
assert([-1,-1] == sol.binarySearchRange([1,2,3,4,5], 9))
assert([2,4] == sol.binarySearchRange([1,2,3,3,3,4,5], 3))
assert([0,2] == sol.binarySearchRange([1,1,1], 1))
print("All test succeeded!")
print("__________________________________________________________________")
