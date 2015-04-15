class Solution:
    # @return a string
    def longestPalindrome(self, s):
        length = len(s)
        pal = [[None] * length for _ in range(length)]
        # base case
        for i in range(length):
            for j in range(i + 1):
                pal[i][j] = 1
        # recursive case with no base included
        for i in range(length -1, -1, -1):
            for j in range(i + 1, length):
                if s[i] == s[j]:
                    pal[i][j] = pal[i+1][j-1]
        # low and high index of current longest palindrome
        lowIndex = -1
        highIndex = -1
        for i in range(length):
            for j in range(length - 1, i , -1):
                if pal[i][j] == 1 and (j-i) >= (highIndex - lowIndex):
                    lowIndex = i
                    highIndex = j
        # Here we found longest substring which is palindrome
        print lowIndex
        print highIndex
        if lowIndex == -1 or highIndex == - 1:
            return s[0]
        return s[lowIndex:highIndex + 1]

sol = Solution()
for str in ["abb", "a", "reddit", "abcbe", "ababacaaaaaaa" , "jglknendplocymmvwtoxvebkekzfdhykknufqdkntnqvgfbahsljkobhbxkvyictzkqjqydczuxjkgecdyhixdttxfqmgksrkyvopwprsgoszftuhawflzjyuyrujrxluhzjvbflxgcovilthvuihzttzithnsqbdxtafxrfrblulsakrahulwthhbjcslceewxfxtavljpimaqqlcbrdgtgjryjytgxljxtravwdlnrrauxplempnbfeusgtqzjtzshwieutxdytlrrqvyemlyzolhbkzhyfyttevqnfvmpqjngcnazmaagwihxrhmcibyfkccyrqwnzlzqeuenhwlzhbxqxerfifzncimwqsfatudjihtumrtjtggzleovihifxufvwqeimbxvzlxwcsknksogsbwwdlwulnetdysvsfkonggeedtshxqkgbhoscjgpiel"]:
    print ("longest palindrome in {}: {}".format(str, sol.longestPalindrome(str)))
