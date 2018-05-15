import time
import pandas as pd


def deriv(coef):
	for i, e in enumerate(coef):
		coef[i] = e*i
	return coef[1:]

def nthDerivative(coef, n, x):
	for i in range(n):
		coef = deriv(coef)
	total = 0
	for j, k in enumerate(coef):
		total += k*(x**j)
	return total % (10**9 + 7)

# test_set =  [91, 13, -62, 17, -93, 91, -56, 100, -6, 1, -8, -70, -58, -47, 25, 1, -34, -33, -84, -100, -63, -89, 90, -40, 66, -92, 82, 9, -27, -77, 79, 25, -76, -91, -22, 12, -64, 7, 64, 51, 40, -30, 81, -40, -53, -65, 53, 59, 30, -78]
poly_degrees = range(1, 12, 1)
test_set = []
for d in poly_degrees:
# 	print d
	test_set.append(range(5*d))
# 	print test_set

# print test_set
results_df = pd.DataFrame()
for poly_coefs in test_set:
# 	print '-/- '* 12
# 	print poly_coefs
	start_time = time.time()
	deriv_degrees = range(0, len(poly_coefs), 1)
	for n in deriv_degrees:
		x = 1
		ans = nthDerivative(poly_coefs, n, x)
		ans_rec = {'polycoefs': poly_coefs,\
					'nth_deriv': n,\
					'x': x,\
					'time': time.time() - start_time,\
					'ans': ans}
		print '+-- '* 15
		print ans_rec
		results_df.append(ans_rec, ignore_index=True)
results_df.reset_index(drop=True)
results_df.columns = ['polycoefs', 'nth_deriv', 'x', 'time', 'ans']