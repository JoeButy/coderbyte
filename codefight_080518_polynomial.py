def deriv(coef):
	for i, e in enumerate(coef):
		coef[i] = e*i
		print coef, e, i
	return coef[1:]

def nthDerivative(coef, n, x):
	for i in range(n):
		print i
		coef = deriv(coef)
		print coef
	total = 0
	for j, k in enumerate(coef):
		total += k*(x**j)
	return total % (10**9 + 7)

test_set =  [4, -9, -6, -4, -5, -6, -5, -3, 7, 4, 8, -4, -10, 7, -10]
nthDerivative(test_set, 5, 0)