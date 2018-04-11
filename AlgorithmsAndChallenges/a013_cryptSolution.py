'''
A cryptarithm is a mathematical puzzle for which the goal is to find 
the correspondence between letters and digits, such that the given arithmetic 
equation consisting of letters holds true when the letters are converted to digits.

You have an array of strings crypt, the cryptarithm, and an an array containing 
the mapping of letters and digits, solution. The array crypt will contain three 
non-empty strings that follow the structure: [word1, word2, word3], which should 
be interpreted as the word1 + word2 = word3 cryptarithm.

If crypt, when it is decoded by replacing all of the letters in the 
cryptarithm with digits using the mapping in solution, becomes a valid 
arithmetic equation containing no numbers with leading zeroes, the answer 
is true. If it does not become a valid arithmetic solution, the answer is false.

Example

For crypt = ["SEND", "MORE", "MONEY"] and

solution = [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]
the output should be
isCryptSolution(crypt, solution) = true.

When you decrypt "SEND", "MORE", and "MONEY" using the mapping given in 
crypt, you get 9567 + 1085 = 10652 which is correct and a valid 
arithmetic equation.

For crypt = ["TEN", "TWO", "ONE"] and

solution = [['O', '1'],
            ['T', '0'],
            ['W', '9'],
            ['E', '5'],
            ['N', '4']]
the output should be
isCryptSolution(crypt, solution) = false.

Even though 054 + 091 = 145, 054 and 091 both contain leading zeroes, 
meaning that this is not a valid solution.

Guaranteed constraints:
crypt.length = 3,
1 ≤ crypt[i].length ≤ 14.

'''

def isCryptSolution(crypt, solution):
	isValid = True
	# let's put out arrays of array solution into dictionary format
	solution = dict((x[0], x[1]) for x in solution)
	array = []
	for word in crypt:
		# now convert the word in crypt based on the solution if it exists
		word = "".join(solution[i] for i in word if i in solution)
		# now add it into our array
		array.append(word)
		# This is to check if there's no leading zeros, if there is, then answer is false
		if word[0] == '0' and len(word)>1:
			isValid = False
	# now we make a list of ints from the array by using map
	# Map applies a function to all the items in an input_list. in our case convert to int
	array = list(map(int, array))
	if (array[0] + array[1]) != array[2]:
		isValid = False
	return isValid



# Here's another person's solution, wow this looks complicated
def isCryptSolution2(crypt, solution):
	'''
		The ord() method returns an integer representing Unicode code 
		point for the given Unicode character. 

		From what it looks like within the solution, we are create a dictionary 
		with value of integer of unicode value of letters with the numbers on right
		e.g.: 'O' would be converted to 79 and it's paired with '1'
	'''
    dic = {ord(c): d for c, d in solution}
    '''
		*v collects all the positional arguments in a tuple
		: is the delimiter of the slice syntax to 'slice out' sub-parts in sequences , [start:end]
		translate: Returns a copy of the string with characters mapped through the given translation table or deleted
		So, this creates a variable that stores in the tuples of crypt values and it's solution values
    '''
    *v, = map(lambda x: x.translate(dic), crypt)
    # and this returns only if v values does not start with 0 and the added values matches the 3rd
    return not any(x != "0" and x.startswith("0") for x in v) and \
        int(v[0]) + int(v[1]) == int(v[2])


# Here's another solution
def isCryptSolution3(crypt, solution):
	'''
		In simple terms, the maketrans() method is a static method that creates 
		a one to one mapping of a character to its translation/replacement.

		It creates a Unicode representation of each character for translation.

		This translation mapping is then used for replacing a character to its 
		mapped character when used in translate() method.
	'''
    table = str.maketrans(dict(solution))
    t = tuple(s.translate(table) for s in crypt)
    zeroes = any(s[0] == '0' for s in t if len(s) > 1)
    return not zeroes and int(t[0]) + int(t[1]) == int(t[2])

# and final solution someone else wrote
def isCryptSolution4(crypt, solution):
    crypt_s = crypt
    for i in range(0, 3):
        for s in solution:
            crypt_s[i] = crypt_s[i].replace(s[0], s[1])
        
        if crypt_s[i] != '0' and crypt_s[i][0] == '0':
            return False
        
    if int(crypt_s[0]) + int(crypt_s[1]) != int(crypt_s[2]):
        return False
    
    return True



if __name__=="__main__":
	crypt = ["TEN", "TWO", "ONE"]
	solution = [['O', '1'],
	            ['T', '0'],
	            ['W', '9'],
	            ['E', '5'],
	            ['N', '4']]

	crypt2 = ["SEND", "MORE", "MONEY"]
	solution2 = [['O', '0'],
	            ['M', '1'],
	            ['Y', '2'],
	            ['E', '5'],
	            ['N', '6'],
	            ['D', '7'],
	            ['R', '8'],
	            ['S', '9']]

    # This should give false
	print(isCryptSolution(crypt, solution))
	# This should give true
	print(isCryptSolution(crypt2, solution2))
