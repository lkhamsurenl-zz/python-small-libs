class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        if len(s) <= 1:
            return True
        map1 = {} # mapping from s to t
        map2 = {} # mapping from t to s
        for i in range(len(s)):
            if s[i] in map1: #
                if map1[s[i]] != t[i]:
                    return False # trying to map to different value
            else: # NEW CHARACTER
                if t[i] in map2: # char has been already mapped
                    return False
                else:
                    map1[s[i]] = t[i] # add to map1
                    map2[t[i]] = s[i] # add to map2
        return True

sol = Solution()
for pair in [["foo", "bar"], ["bar", "foo"], ["egg", "add"], ["a", "b"], ["a", "aba"], ["red", "aba"]]:
    print("{} and {} are isomorphic: {}".format(pair[0], pair[1], sol.isIsomorphic(pair[0], pair[1])))
