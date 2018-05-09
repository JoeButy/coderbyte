def checkPalindrome(inputString):
	l = len(inputString)
	h = int(l/2)
	return inputString[:h:1] == inputString[:l-h-1:-1]
