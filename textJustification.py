class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        if len(words) == 0:
            return ""
        justified = [] # collect the result
        currInd = 0 # current index scanning
        isLastLine = False # indicate the last line
        while currInd < len(words):
            lastFitInd = currInd # index that can fit
            length = L - len(words[currInd]) # available length
            while lastFitInd + 1< len(words) and (length - 1 - len(words[lastFitInd + 1])) >= 0:
                length = length - (1 + len(words[lastFitInd + 1]))
                lastFitInd = lastFitInd + 1
            numOfWords = lastFitInd - currInd + 1
            string = words[currInd] # current Line
            currInd = currInd + 1 # since currInd has been added
            if lastFitInd + 1 == len(words):
                isLastLine = True
            if isLastLine or numOfWords == 1: # no additional space to even out
                additionalSpace = 0
            elif numOfWords != 1:
                additionalSpace = (length / (numOfWords - 1))
            length = length - additionalSpace * (numOfWords - 1) # leftover
            #print ("added space: {} {}".format(additionalSpace, numOfWords))
            while currInd <= lastFitInd:
                string = string + " " * (additionalSpace + 1) # even distribute
                if length > 0 and not isLastLine:
                    string = string + " "
                    length = length - 1 # put space in the front
                string = string + words[currInd] # add the word
                currInd = currInd + 1
            # get rid of extra space at the end
            if length != 0:
                string = string + " "*length # all left space should be placed
            #print "|" + string + "|"
            justified.append(string)
            #length = L # start over
        return justified

sol = Solution()
print "1. Simple case:"
print sol.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)

print "2. 1 word case:"
print sol.fullJustify(["This"], 5)

print "3. leftovers:"
print sol.fullJustify(["This"], 6)

print "4. No additional space available:"
print sol.fullJustify(["This", "is", "mine"], 4)

print "5. Last line should be left justified"
print sol.fullJustify(["What", "must", "be", "shall", "be."], 12)

print "6. Check on the even distribution: "
print sol.fullJustify(["Give","me","my","Romeo;","and,","when","he","shall","die,","Take","him","and","cut","him","out","in","little","stars,","And","he","will","make","the","face","of","heaven","so","fine","That","all","the","world","will","be","in","love","with","night","And","pay","no","worship","to","the","garish","sun."], 25)
