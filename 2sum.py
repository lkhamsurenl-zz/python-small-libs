import itertools
# Fund 2 indices such that the numbers add up to target
class Sum:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        dic = {} # includes remaining value to adding to target
        for i in range(len(nums)):
            if nums[i] in dic:
                # we found the number in there
                return [dic[nums[i]], i]
            else:
                dic[target - nums[i]] = i
        return [] # if no such number exist
    def threeSum(self, nums):
        nums.sort()
        ans = []
        for i in range(len(nums)):
            # i is the smallest value
            j = i + 1 # iterate from the next elt
            k = len(nums) - 1 # last elt
            while j < k:
                curr = nums[i] + nums[j] + nums[k]
                if curr == 0: # we found the sum
                    ans.append([nums[i], nums[j], nums[k]])
                    j = j + 1
                    k = k - 1
                elif curr < 0:
                    j = j + 1
                else:
                    k = k - 1
        return list(ans for ans, _ in itertools.groupby(ans))

    def fourSum(self, nums, target):
        """
        Find all 4 numbers adding up to target
        """
        output = []
        nums.sort() # nlogn
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                k = j + 1
                l = n - 1
                while k < l:
                    s = nums[i] + nums[j] + nums[k] + nums[l]
                    if s == target:
                        # found the value
                        output.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                    elif s < target: # increase the value
                        k += 1
                    else:
                        l -= 1 # decrease since it's more than target
        return list(k for k, _ in itertools.groupby(output))

s = Sum()
# Tests for 2 sum
for (l, target, want) in [([1,2,3], 0, []), ([1,2], 3, [0, 1])]:
    got = s.twoSum(l, target)
    assert got == want, \
        "twoSum({}, {}) = {}, want {}".format(l, target, got, want)
# Tets 3 sum
for (l, want) in [([1,2,3], []), ([1,-4,3], [[-4, 1, 3]]), ([1,0,-1,2, -2],[[-2, 0, 2], [-1, 0, 1]]), ([1,0,-1,1, -1], [[-1, 0, 1]])]:
    got = s.threeSum(l)
    assert got == want, \
        "threeSum({}) = {}; want {}".format(l, got, want)
# Test 4 sum
for (l, target, want) in [([1,2,3], 7, []), ([1,-4,3, 2], 2, [[-4, 1, 2, 3]]), ([1,0, 0,-1,2, -2], 0, [[-2, -1, 1, 2], [-2, 0,0, 2], [-1, 0,0, 1]])]:
    got = s.fourSum(l, target)
    assert got == want, \
        "fourSum({}, {}) = {}; want {}".format(l,target, got, want)


