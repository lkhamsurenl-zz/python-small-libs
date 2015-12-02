# This file contains problems directly pertained to list problems.
class List(object):
	def alternatingList(self, lst):
		"""
		Given a list, alternate it in place to a1 < a2 > a3 < a4 > a5 ...
		"""
		if len(lst) < 2:
			return
		if lst[0] > lst[1]:
			self.__swap(lst, 0, 1)
		for i in range(0, len(lst) - 2):
			if lst[i] < lst[i+1] < lst[i+2] or lst[i] > lst[i+1] > lst[i+2]:
				self.__swap(lst, i + 1, i + 2)
		return lst

	def firstMissingPositive(self, lst):
		"""
		Given a lst, find a first missing positive. 
		[0,1,4] -> 2
		[1,2,3] -> 4
		"""
		if len(lst) == 0:
			return 1
		# place all the positive numbers in a correct place in the lst
		for i in range(len(lst)):
			if 0 < lst[i] <= len(lst) and lst[lst[i] - 1] != lst[i]:
				self.__swap(lst, i, lst[i] - 1)
		for i in range(len(lst)):
			if lst[i] != i + 1: # The + number @ this position is missing.
				return i + 1
		return len(lst) + 1

	def __swap(self, lst, i, j):
		temp = lst[i]
		lst[i] = lst[j]
		lst[j] = temp

	def longestConsecutive(self, lst):
		"""
		Given a list, find the length of the longest consecutive numbers.
		"""
		if len(lst) < 2:
			return len(lst)
		d = {} # keep track of pointer to the previous value
		for num in lst:
			d[num] = 1
		longest = 0 # length of the longest
		for num in lst:
			if num in d:
				# find the smallest element in the current chain
				while num in d:
					num -= 1
				# num + 1 is the smallest that exist in dict
				num += 1
				length = 0
				while num in d:
					length += 1
					d.pop(num, None) # remove to avoid visiting again
					num += 1
					# This allows visiting each consecutive list only once.
				if length > longest:
					longest = length # update the longest list we've seen so far
		return longest

#############################    TEST 		###################################
lst = List()
#######							Alternating List 				##############
for (got, want) in [ ([1,2,3], [1,3,2]), ([3,2,1], [2,3,1]),\
					([6,5,4,3,2,1], [5,6,3,4,1,2]), ([1,2], [1,2]), ([2,1], [1,2]) ]:
	got = lst.alternatingList(got)
	assert got == want, \
		"alternatingList(lst) = {}; want: {}".format(got, want) 

#######							First Missing Positive 		     ##############
for (l, want) in [ ([1,2,3], 4), ([3,2,1], 4), ([0,2], 1), ([0,1,2], 3), ([], 1),\
					([1,1,2], 3) ]:
	got = lst.firstMissingPositive(l)
	assert got == want, \
		"firstMissingPositive({}) = {}; want: {}".format(l, got, want) 

#######				       Length of longest consecutive 		 ##############
for (l, want) in [ ([1,2,3], 3), ([3,2,1], 3), ([0,2], 1), ([0,1,2], 3), ([], 0),\
					([200, 3, 199, 2, 100, 1], 3) ]:
	got = lst.longestConsecutive(l)
	assert got == want, \
		"longestConsecutive({}) = {}; want: {}".format(l, got, want) 
