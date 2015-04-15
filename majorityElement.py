class Solution:
    # @return an integer
    def majorityElement(self, num):
        major = num[0] # majority we have seen so far
        numOcc = 1
        for i in range(1, len(num)):
            if numOcc == 0: # majority element is no longer the current one
                major = num[i]
                numOcc = 1
            elif major == num[i]:
                numOcc = numOcc + 1
            else:
                numOcc = numOcc -1 # since there is one more elt not majority
        return major
sol = Solution()
for arr in [[1, 1, 2, 2, 2], [1, 1, 2, 2], [1, 1,1,2,1,1,1,2,2,3,2, 7, 6, 1,1]]:
    print ("majority of {} is: {}".format(arr , sol.majorityElement(arr)))
