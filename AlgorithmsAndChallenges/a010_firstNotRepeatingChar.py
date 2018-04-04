def firstNotRepeatingCharacter(s):
	order = []
	count = {}
	# If we encounterd number before we increment by 1
	for x in s:
		if x in count:
			count[x] += 1
		# if not we add it into our list
		else:
			count[x] = 1
			order.append(x)
	# Now we look into out list, if 1, means non repeating num
	for x in order:
		if count[x] == 1:
			return x
	return "_"

testVar = "abacabad"
print(firstNotRepeatingCharacter(testVar))


# A solution from another person using rindex
'''
rindex
The method rindex() returns the last index where the substring str is found, 
or raises an exception if no such index exists, optionally restricting 
the search to string[beg:end].
'''
def firstNotRepeatingCharacter2(s):
	for c in s:
		if s.index(c) == s.rindex(c):
			return c
	return '_'