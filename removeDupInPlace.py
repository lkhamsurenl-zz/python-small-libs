class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        numOccurences = 0
        for num in A:
            if num == elem:
                numOccurences = numOccurences + 1

        length = len(A)
        dup = length - 1
        nonDup = length - 1 - numOccurences
        while nonDup >= 0 and dup > length - 1 - numOccurences:
            print ("{} and {}".format(nonDup, dup))
            if A[dup] == elem:
                dup = dup - 1
            if A[nonDup] == elem:
                temp = A[nonDup]
                A[nonDup] = A[dup]
                A[dup] = temp

                nonDup = nonDup -1
                dup = dup -1
            else:
                nonDup = nonDup - 1
        return A
        #return length - numOccurences

sol = Solution()
for A in [[1, 2, 2, 2, 3, 4], [2, 2 ,3], [1,1,2,2,3,4,5,6,2,1,2,3,5,6,2]]:
    print ("new length is: {}".format(sol.removeElement(A, 2)))
