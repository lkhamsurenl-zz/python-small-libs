class Solution:
    # @param A, a list of integers, which can include duplicate elements
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        rotationIndex = self.searchIndex(A, 0, len(A) - 1)
        print rotationIndex
        if target == A[0]:
            return 0
        elif target > A[0]:
            return self.binarySearch(A, 0, rotationIndex, target)
        else:
            return self.binarySearch(A, rotationIndex + 1, len(A) -1 , target)

    def searchIndex(self, A, low, high):
        mid = low + (high - low) / 2
        if mid  +1 >= len(A) or A[mid] > A[mid + 1]:
            return mid
        if A[low] == A[mid]: # rotation could be in any side
            return self.searchIndex(A, low, mid - 1) if not self.allSame(A, low, mid) else self.searchIndex(A, mid + 1, high)
        elif A[low] <= A[mid]:
            return self.searchIndex(A, mid + 1, high)
        else:
            return self.searchIndex(A, low, mid - 1)

    def binarySearch(self, A, low, high, target):
        if low > high:
            return -1
        mid = low + (high - low) /2
        if A[mid] == target:
            return mid
        elif A[mid] < target:
            return self.binarySearch(A, mid + 1, high, target)
        else:
            return self.binarySearch(A, low, mid - 1, target)

    def allSame(self, A, low, high):
        curr = low
        while curr <= high:
            if A[curr] != A[low]:
                return False
            curr = curr + 1
        return True

sol = Solution()
arr = [10, 10, 10, 10, 1, 10, 10, 10]
print sol.search(arr, 10)
