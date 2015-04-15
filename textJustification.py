class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        if len(words) == 0:
            return ""
        justified = []
        currInd = 0
        while currInd < len(words):
            lastFitInd = currInd
            length = L
            while lastFitInd < len(words) and length - 1 - len(words[lastFitInd]) >= 0:
                length = length - 1 - len(words[lastFitInd])
                lastFitInd = lastFitInd + 1
            length = length + 1 # since we subtracted one additional space
            # we found how many string would fit
            # length is available space left
            st = ""
            numOfWords = lastFitInd - currInd
            addedSpace = length / (numOfWords )
            print ("added space: {} {}".format(addedSpace, numOfWords))
            while currInd < lastFitInd:
                st = st + words[currInd] + " "
                if length > 0:
                    print length
                    st = st + " " * (addedSpace + 1) # add space
                    length = length - addedSpace
                currInd = currInd + 1
            # get rid of extra space at the end
            print "|" + st[:L +1] + "|"
            justified.append(st[0:L])
            length = L
        return justified

sol = Solution()
print sol.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
