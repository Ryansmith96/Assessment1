

def one(input1, input2):
	in1len = len(input1)
	in2len = len(input2)
	if in1len > in2len:
		return input1
	if in1len < in2len:
		return input2
	if in1len == in2len:
		return (input1 + " " + input2)
	

print(one("hi","hello"))

def two(input):
	return ""

def three(arg1):
	if arg1%3==0 and arg1%5==0:
		return "fizzbuzz"
	if arg1%3==0:
		return "fizz"
	if arg1%5==0:
		return "buzz"
	else:
		return "null"




def four(arg1):
	foursplit = four.split()
	bigger = 0
	for i in foursplit:
		value = 0
		for d in i:
			value = value + int(d)
	if value > bigger:
		bigger = value
	return bigger

	

# def five(input):
# 	return []


# def six(input):
# 	if "ie" in input:


	
#     return False


def seven(input):
	vowels = "aeiouAEIOU"
	vowelcount = 0
	for s in input:
		if s in vowels:
			vowelcount = vowelcount + 1
	return vowelcount


def eight(input):
	numlist = []
	result = 0
	for i in input:
		numlist.append(i)
		for b in numlist:
			result = result * b
	return result


# def nine(inputString, char):
# 	spaceless = inputString.replace(" ", "")
# 	pos = spaceless.find(char)
# 	return pos

def nine(inputString, char):
	spaceless = inputString.replace(" ", "")
	if char not in inputString:
		return -1
	for i in range(len(spaceless)):
 		if (spaceless[i] == char):
			return i+1
	

 
# def ten(string, int, char):
# 	splitstring = string.split()
# 		if 
# 	return False
