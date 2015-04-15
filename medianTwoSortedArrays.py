class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        return self.recFindMedian(A, 0, len(A) - 1, B, 0, len(B)  - 1)

    def recFindMedian(self, A, lowA, highA, B, lowB, highB):
        midA = lowA + (highA - lowA)/2
        midB = lowB + (highB - lowB)/2
        if lowA == midA and midA == highA:
            return self.findMedian(A[lowA], B, lowB, highB)
        if lowB == midB and midB == highB:
            return self.findMedian(B[lowB], A, lowA, highA)
        if A[midA] == B[midB]:
            return A[midA]
        if A[midA] < B[midB]:
            return self.recFindMedian(A, midA, highA, B, lowB, midB)
        else:
            return self.recFindMedian(A, lowA, midA, B, midB, highB)
    def findMedian(self, num, A, lowA, highA):
        index = self.findIndex(num, A, lowA, highA)
        mid = lowA + (highA - lowA ) / 2
        if index < mid:
            return A[mid]
        else:
            return A[mid + 1]
    def findIndex(self, num, A, lowA, highA):
        if lowA > highA:
            return lowA
        mid = lowA - (highA - lowA) / 2
        if mid + 1 > highA  or A[mid] <= num and num <= A[mid + 1]:
            return mid
        if A[mid] < num:
            return self.findIndex(num, A, mid + 1, highA)
        else:
            return self.findIndex(num, A, lowA, mid - 1)

sol = Solution()
print sol.findMedianSortedArrays([1, 2, 3, 4, 5], [5, 5,6,7, 10, 10])
