class Solution:
# @return an integer
    def reverse(self, x):
        if x < 10 and x > - 10:
            return x #
        retVal = 0
        neg = True if x < 0 else False
        x = abs(x)
        numDig = self.countDigits(x)
        for i in range(numDig):
            digit = x % 10 # current digit
            x = x / 10 # get the leftover from x
            retVal = retVal + digit * pow(10, numDig - 1 - i) # put current digit into position
        # Check the overflow
        if retVal > pow(2, 31) - 1:
            return 0
        retVal = (0 - retVal) if neg else retVal
        return retVal

    # number of digits in number, assume x is not digit by itself and nonnegative number
    def countDigits(self, x):
        numDigits = 0
        curr = x
        while curr is not 0:
            curr = curr / 10
            numDigits = numDigits + 1
        return numDigits


sol = Solution()
print ("reverse of 10 is: {}".format(sol.reverse(10)))
print ("reverse of 123 is: {}".format(sol.reverse(123)))
print ("reverse of -123 is: {}".format(sol.reverse(-123)))
