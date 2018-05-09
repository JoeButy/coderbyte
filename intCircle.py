def intCircle(r):
	ans = 0
	for x in range(1, int(r)+1):
		for y in range(0, int(r)+1):
			if x**2 + y**2 <= r**2:
				ans += 1
				print x, y, r
	print ans
	return ans*4+1

for i in range(6):
	print 'r:', i
	print intCircle(i)