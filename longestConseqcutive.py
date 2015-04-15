class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        dic = {}
        for val in num:
            dic[val] = 1 # put the number in dic
        longest = 0
        for val in num:
            if val in dic:
                minimal = val
                while minimal - 1 in dic:
                    minimal = minimal - 1
                # increment and remove from the dic
                currLength = 0
                while minimal in dic:
                    # remove from the dic
                    dic.pop(minimal)
                    minimal = minimal + 1
                    currLength = currLength + 1
                if longest < currLength:
                    longest = currLength
        return longest

sol = Solution()
print sol.longestConsecutive([100, 1, 200, 4, 3, 2])
