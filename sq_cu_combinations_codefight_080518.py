from itertools import permutations

def perfectSquareOrCube(n):
	ls = list(str(n))
	match = 0
	perms = set(list(permutations(ls, len(ls))))
	for p in perms:
		ds = ''
		for d in p:
			ds += d
		num = int(ds)
# 		print num
		sq = int(num)**(1./2)
		cu = int(num)**(1./3)
# 		print num, cu, int(round(cu)), abs(int(cu) - cu)
		if abs(int(round(sq)) - sq) < .000001:
			match += 1
			print 'sq:', num, sq
		elif abs(int(round(cu)) - cu) < .000001:
			print 'cu:', num, cu
			match += 1
		else:
			pass
	return match


test_set = [441,54,71,250,64,521]

for i in test_set:
	print perfectSquareOrCube(i)