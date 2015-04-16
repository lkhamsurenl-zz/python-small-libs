# If largest power of 2 leq to m is pow, then m should be only one pow of 2
# All numbers would include pow(2, pow) as most significant bit
# then recurse
class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def rangeBitwiseAnd(self, m, n):
        if m > n:
            return 0
        # the only power of 2 can be m
        power = self.findPower(m)
        if n < pow(2, power + 1):
            return pow(2, power) + self.rangeBitwiseAnd(m - pow(2, power), n - pow(2, power))
        return 0
    # finds the largest power of two, which is not greater than m
    def findPower(self, m):
        power = 0
        while m > pow(2, power):
            power = power + 1
        return power if m == pow(2, power) else power - 1

sol = Solution()
print sol.rangeBitwiseAnd(18, 19)
