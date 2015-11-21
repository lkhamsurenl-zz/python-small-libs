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

#######################				Test 			##########################
s = Strings()
for (num, want) in [ ("123", True), ("101", True), ("111", False), ("112358", True) ]:
	got = s.additiveNumber(num)
	assert got == want, \
		"additiveNumber({}) = {}; want {}".format(num, got, want)