def singleNumber(lst):
	"""
	Given a list of numbers s.t each number appear exactly twice only one appear
	once. Find the number.
	"""
	# Bitwise xor operation would cancel out each bit appear twice, which means
	# only appearing number's all 1's will survive
	xor = 0
	for num in lst:
		xor ^= num
	return xor

def singleNumber2(lst):
	"""
	Given a list of numbers s.t each number appear exactly twice except two that
	appear exactly once. Find those numbers.
	"""
	# xor will give us xor of two unique numbers.
	# Since those 2 are not equal, there is a position in bit repr. that they
	# differ in value. 
	xor = 0
	for num in lst:
		xor ^= num
	# last active bit of xor repr. the differing value.
	# xor = 100101100 -> xor ^ (xor - 1) = 000000011
	# xor ^ (xor - 1) + 1 >> 1 = 100 
	diff = ((xor ^ (xor - 1)) + 1) >> 1
	groupA = 0
	groupB = 0
	for num in lst:
		if num & diff:
			groupA ^= num
		else:
			groupB ^= num
	return set([groupA, groupB])

def countBits(num):
	"""
	Count the number of 1s in binary form for each number 0 <= i <= num.
	"""
	counts = [0] # 0's binary has 0 ones.
	power = 0 # current power of the number.
	while 2 ** power <= num:
		counts.append(1) # Any power of 2 has exactly 1 one.
		for i in range(1, 2 ** power):
			if 2 ** power + i > num:
				# added all the ones, done.
				break
			else:
				counts.append(counts[i] + 1)
		power += 1
	return counts 

################################ TEST  #########################################

################################ Single Number #################################
for (want, lst) in [(2, [1,2,3,1,3]), (1, [1,-2,-2,3,3]), (0, [0,1,1])]:
	got = singleNumber(lst)
	assert got == want, \
		"singleNumber({}) = {}; want: {}".format(lst, got, want)

################################ TEST  #########################################
for (lst, want) in [([1,2,3,3], set([1,2])), ([4,5,4,5,1,2], set([1,2])), \
	([4,6,4,1,1,3,3,5], set([6,5]))]:
	got = singleNumber2(lst)
	assert got == want, \
		"singleNumber2({}) = {}; want: {}".format(lst, got, want)

################################ Count bits #################################
for (num, want) in [(2,[0,1,1]), (3,[0,1,1,2]), (10,[0,1,1,2,1,2,2,3,1,2,2]), \
	(16, [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1])]:
	got = countBits(num)
	assert got == want, \
		"countBits({}) = {}; want: {}".format(num, got, want)
