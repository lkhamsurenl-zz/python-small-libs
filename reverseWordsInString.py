class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        # get all the words
        lst = s.split(" ") # NOTE: there are parts with length 0
        lst = [i for i in lst if len(i) != 0]
        # reverse the list
        low = 0
        high = len(lst) - 1
        while low < high:
            if len(lst[low]) != 0 and len(lst[high]) != 0:
                temp = lst[low]
                lst[low] = lst[high]
                lst[high] = temp
                low = low + 1
                high = high - 1
            elif len(lst[low]) == 0:
                low = low + 1
            else:
                high = high - 1
        # construct back the string
        return " ".join(lst)
