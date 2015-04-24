# happy number is the number sum of digits recursively added is 1
class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        lst = [n] # keep track of visited numbers
        while True:
            if n == 1:
                return True # found the number
            sumOfDigits = 0
            num = n
            while num != 0:
                digit = num % 10
                sumOfDigits = sumOfDigits + pow(digit, 2)
                num = num / 10
            if sumOfDigits in lst:
                return False # repeated number -> loop
            else:
                lst.append(sumOfDigits)
                n = sumOfDigits # start over

sol = Solution()
for num in [1, 0, 4, 16, 19, 29]:
    print("{} : {}".format(num, sol.isHappy(num)))
