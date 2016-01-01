import copy
# This file contains problems directly pertained to list problems.
class List(object):
	def alternatingList(self, lst):
		"""
		Given a list, alternate it in place to a1 < a2 > a3 < a4 > a5 ...
		"""
		if len(lst) < 2:
			return
		if lst[0] > lst[1]:
			self.__swap__(lst, 0, 1)
		for i in range(0, len(lst) - 2):
			if lst[i] < lst[i+1] < lst[i+2] or lst[i] > lst[i+1] > lst[i+2]:
				self.__swap__(lst, i + 1, i + 2)
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
				self.__swap__(lst, i, lst[i] - 1)
		for i in range(len(lst)):
			if lst[i] != i + 1: # The + number @ this position is missing.
				return i + 1
		return len(lst) + 1

	def __swap__(self, lst, i, j):
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

	def move_target_back(self, lst, target):
		"""
		Move all the target values to the back of the array:
		[1,2,1,0,4], 1 -> [2,0,4,1,1]
		"""
		non_target = 0 # next non-target value should be placed at this index.
		for i in range(len(lst)):
			if lst[i] != target:
				lst[non_target] = lst[i]
				non_target += 1
		# non_target is the last index 
		while non_target < len(lst):
			lst[non_target] = target 
			non_target += 1

	def remove_duplicates(self, lst):
		"""
		Remove all duplicates from an array.
		[1,1,2,3,3] -> [1,2,3]
		Assume the given array is sorted.
		@return: size of the non duplicate part of an array
		"""
		nondup = 1
		for i in range(1, len(lst)):
			if lst[i] != lst[i - 1]:
				lst[nondup] = lst[i]
				nondup += 1
		return nondup


	def summary_ranges(self, lst):
		"""
		Given list of integers, find summary ranges:
		[1,2,3,5,6,9] -> ["1->3", "5->6", "9"]
		"""
		lst.sort() # Sort in case it is not sorted
		start = 0
		summary = [] # Holds summary output.
		for i in range(1, len(lst)):
			if lst[i] - lst[i - 1] > 1:
				# No longer consecutive, so make a range.
				current_range = "{}->{}".format(lst[start], lst[i-1]) if start != i - 1 else \
					"{}".format(lst[start])
				summary.append(current_range)
				start = i # Increment the start point.
		current_range = "{}->{}".format(lst[start], lst[len(lst)-1]) if start != len(lst) - 1 else \
					"{}".format(lst[start])
		summary.append(current_range)
		return summary

	def rotate(self, lst, k):
		"""
		Rotate given list by k position:
		[1,2,4,5], 2 -> [4,5,1,2]
		"""
		if k == 0:
			return
		# [1,2,4,5] -> [5,4,2,1]
		self.__flip__(lst, 0, len(lst) - 1)
		# [5,4,2,1] -> [4,5, 2,1]
		self.__flip__(lst, 0, k - 1)
		# [4,5, 2,1] -> [4,5, 1,2]
		self.__flip__(lst, k, len(lst) - 1)

	def __flip__(self, lst, low, high):
		"""
		Flip a given array between low and high (inclusive)
		"""
		while low < high:
			self.__swap__(lst, low, high)
			low += 1
			high -= 1

	def productExceptSelf(self, lst):
		"""
		return products except itself for each number in lst
		[1,2,3] -> [2*3,1*3,1*2]
		"""
		prefix = copy.deepcopy(lst) # product of elts lst[:i]
		postfix = copy.deepcopy(lst) # product of elts lst[i:]
		for i in range(1, len(lst)):
			prefix[i] *= prefix[i -1]
			postfix[len(lst) - i - 1] *= postfix[len(lst) - i]
		for i in range(len(lst)):
			pre = prefix[i - 1] if i != 0 else 1
			post = postfix[i + 1] if i != len(lst) - 1 else 1
			lst[i] = pre * post

	def wiggleSort(self, lst):
		if len(lst) < 2:
			return
		if lst[0] > lst[1]:
			self.__swap__(lst, 0, 1)
		for i in range(1, len(lst) -1):
			if lst[i-1] <= lst[i] <= lst[i+1] or lst[i-1] >= lst[i] >=lst[i+1]:
				self.__swap__(lst, i, i+1)

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

#######				       Move target values back 		 ##############
for (got, target,  want) in [ ([1,2,1,4,0,1], 1, [2,4,0,1,1,1]), ([1,1,1], 1, [1,1,1]),\
						([1,1], 2, [1,1]), ([1,4,0], 0, [1,4,0]) ]:
	inp_arr = copy.deepcopy(got)
	lst.move_target_back(got, target)
	assert got == want, \
		"move_target_back({}, {}) = {}; want: {}".format(inp_arr, target, got, want)

###########						Summary Ranges 				################
for (arr, want) in [ ([1,2,3], ["1->3"]), ([3,1,2], ["1->3"]), ([7,1,3,2,6,9], ["1->3", "6->7", "9"]) ]:
	got = lst.summary_ranges(arr)
	assert got == want, \
		"summary_ranges({}) = {}; want: {}".format(arr, got, want)

###########						Remove duplicates 				################
for (got, want) in [ ([1,2,3], [1,2,3]), ([1,1], [1]), ([1,2,2,3,3,4], [1,2,3,4]) ]:
	input_array = copy.deepcopy(got)
	length = lst.remove_duplicates(got)
	assert got[:length] == want, \
		"remove_duplicates({}) = {}; want: {}".format(input_array, got, want)

###########						Remove duplicates 				################
for (got, k, want) in [ ([1,2,3], 0, [1,2,3]), ([1,1], 1, [1,1]), ([1,2,2,3,3,4], 2, [3,4,1,2,2,3]) ]:
	input_array = copy.deepcopy(got)
	length = lst.rotate(got, k)
	assert got == want, \
		"rotate({}) = {}; want: {}".format(input_array, got, want)

for (got, want) in [ ([1,2,3], [6,3,2]), ([1,0,2], [0,2,0]), ([0,0,1], [0,0,0]) ]:
	arr = copy.deepcopy(got)
	lst.productExceptSelf(got)
	assert got == want,\
		"productExceptSelf({}) = {}; want: {}".format(arr, got, want)

############				Wiggle Sort `					##################
for (got, want) in [ ([1], [1]), ([1,2,3], [1,3,2]), ([1,5,1,1,6,4],[1,5,1,6,1,4]),\
	([1,3,2,2,3,1], [1,3,2,3,1,2]), ([1,2,2,1,2,1,1,1,1,2,2,2],[1,2,1,2,1,2,1,2,1,2,1,2]) ]:
	arr = copy.deepcopy(got)
	lst.wiggleSort(got)
	assert got == want, \
		"wiggleSort({}) = {}; want: {}".format(arr, got ,want)


