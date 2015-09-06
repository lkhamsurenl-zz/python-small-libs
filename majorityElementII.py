class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        # there could be at most 2 majority elements, if majority element is defined as having more than [n/3] times
        # we do recursion as follows, find the majority element in 3 equal sizes. If they are equal, then we found one
