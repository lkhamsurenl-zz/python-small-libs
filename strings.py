class Strings(object):
	def additiveNumber(self, num):
		"""
		Given a number in string format, check if digits can form additive sequence:
		"112358" => 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
		"""
		for i in range(1, len(num)):
			if num[0] == "0" and i != 1:
				continue # sequence term cannot start with 0
			for j in range(i + 1, len(num)):
				if num[i] == "0" and j != i + 1:
					continue
				if self.__recAdditiveNumber(num, 0, i, j):
					return True
		return False

	def __recAdditiveNumber(self, num, start, i, j):
		"""
		Recursively check if sequence start:i and i:j can form additiveNumber
		"""
		if j >= len(num):
			return True
		next = str(int(num[start:i]) + int(num[i:j]))
		if next == num[j:j + len(next)]:
			return self.__recAdditiveNumber(num, i, j, j + len(next))
		else:
			return False

	def ser(self, d):
		"""
		Given a dictionary, serialize to a string
		"""
		output = ""
		for key in d.keys():
			val = d[key]
			if isinstance(d[key], dict):
				val = self.ser(d[key]) # recursively serialize if it's dict
			output += "{}:{}".format(key, val)
		return "{" + output + "}"

	def deser(self, s):
		"""
		Given a string, deserialize it to a dict
		"""
		if len(s) == 2:
			return {}
		d = {}
		start = 1 # start index of {
		while start < len(s) - 1:
			i = self.__findKey(s, start)
			key = s[start:i]
			start = i + 1
			i = self.__findValue(s, start)
			value = self.deser(s[start:i])
			d[key] = value
			start = i + 1
		return d

	def __findKey(self, s, start):
		index = start
		while index < len(s):
			if s[index] == ":":
				return index
			index += 1
		return index

	def __findValue(self, s, start):
		index = start	
		while index < len(s):
			if s[index] == "{":
				end = index + 1
				counter = 1
				while counter != 0:
					if s[end] == "{":
						counter += 1
					elif s[end] == "}":
						counter -= 1
					end += 1
				return end
			else:
				index += 1
		return index

	def groupAnagrams(self, strings):
		"""
		Given a list of strings, group anagrams.
		[loop, polo, pool, aba, yo, baa] -> [[loop, polo, pool], [aba, baa], [yo]]
		"""
		mapping = {} # key: sorted string; value: list of anagrams associated 
		# with the given sorted string.
		for s in strings:
			sorted_s = "".join(sorted(s))
			if sorted_s in mapping:
				mapping[sorted_s].append(s)
			else:
				mapping[sorted_s] = [s]

		groups = []
		for key in mapping.keys():
			groups.append(mapping[key])
		return groups

	def isIsomorphic(self, s, t):
		"""
		Given two strings, figure out if they isIsomorphic
		(baa, foo) -> true, (foo, bar) -> false
		"""
		if len(s) != len(t):
			return False
		mapping1 = {} # Holds mapping from s to t.
		mapping2 = {} # Holds mapping from t to s.
		for i in range(len(s)):
			if (s[i] in mapping1 and mapping1[s[i]] != t[i]) or (s[i] not in mapping1 and t[i] in mapping2):
				return False
			# All the other cases are valid, so add the mappings.
			mapping1[s[i]] = t[i]
			mapping2[t[i]] = s[i]
		return True

	def reverseWords(self, s):
		"""
		Given a string, reverse all the words inside
		'I love you' -> 'you love I'
		"""
		words = s.split(" ") # splitted words
		low = 0
		high = len(words) - 1
		while low < high:
			temp = words[low]
			words[low] = words[high]
			words[high] = temp
			low += 1
			high -= 1
		return " ".join(words)

#######################				Test 			##########################
s = Strings()
for (num, want) in [ ("123", True), ("101", True), ("111", False), ("112358", True) ]:
	got = s.additiveNumber(num)
	assert got == want, \
		"additiveNumber({}) = {}; want {}".format(num, got, want)

##################### 		serialize dic 			#######################
for (d, want) in [ ({}, "{}"), ({"a":"b"}, "{a:b}"), ({"a":{"b":"c"}}, "{a:{b:c}}") ]:
	got = s.ser(d)
	assert got == want, \
		"ser({}) = {}; want: {}".format(d, got, want)

##################### 		deserialize dic 			#######################
#for (st, want) in [ ("{}", {}), ("{a:b}", {"a":"b"}), ("{a:{b:c}}", {"a":{"b":"c"}}) ]:
#	got = s.deser(st)
#	assert got == want, \
#		"ser({}) = {}; want: {}".format(st, got, want)

##################### 	Group Anagrams      			#######################
for (st, want) in [ (["pool", "polo", "aba", "baa", "loop"], [["pool", "polo", "loop"], ["aba", "baa"]]) ]:
	got = s.groupAnagrams(st)
	assert got == want, \
		"groupAnagrams({}) = {}; want: {}".format(st, got, want)

#############				isIsomorphic				#####################
for (st, t, want) in [ ("a", "b", True), ("aa", "ab", False), ("foo", "bar", False),\
	("foo", "baa", True), ("bar", "foo", False) ]:
	got = s.isIsomorphic(st,t)
	assert got == want, \
		"isIsomorphic({}, {}) = {}; want: {}".format(st, t, got, want)

for (st, want) in [ ("foo", "foo"), ("I love you", "you love I") ]:
	got = s.reverseWords(st)
	assert got == want, \
		"reverseWords({}) = {}; want: {}".format(st, got, want)