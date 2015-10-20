class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
        	return 0
        sums = [nums[0]]
        for i in range(1, len(nums)):
        	if nums[i] >= s:
        		return 1
        	sums.append(sums[-1] + nums[i]) # append with the current number
        if sums[-1] < s:
        	return -1 # no subarray can match the ss
        # for each number find the index s.t sums[current] - sums[index] >= s
        mIndex = float('inf')
        for cIndex  in range(len(nums) - 1, -1, -1):
        	# do the BS to find the matching index
        	mIndex = min(mIndex, cIndex - self.BS(sums, 0, cIndex -1, sums[cIndex], s))
        return mIndex

    def BS(self, sums, low, high, current, s):
    	if low > high:
    		return len(sums)
    	mid = low + (high - low) / 2
    	if current - sums[mid] >= s and current - sums[mid + 1] < s:
    		return mid
    	if current - sums[mid] > s:
    		return self.BS(sums, mid + 1, high, current, s)
    	else:
    		return self.BS(sums, low, mid - 1, current, s)

sol = Solution()
print(sol.minSubArrayLen(7, [2,3,1,2,4,3]))
assert(2 == sol.minSubArrayLen(7, [2,3,1,2,4,3]))

