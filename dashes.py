def dashes(n):
	'''Create a matrix that has a n width diamond shaped set of dashes and pipes inside
# i:  3
#   -  
#  -|- 
# -|-|-
#  -|- 
#   - 
	'''
	i = 1
	ans = []
	while len(ans) < 2 * n - 1:
		row = ''
		i = len(ans)
		if i >= n:
			for a in range(n-1, 0, -1):
				ans += [ans[n - 1 - abs(n - a)]]
		else:
			while len(row) < 2 * n - 1:
				j = len(row)
				if j >= n:
					for k in range(n-1, 0, -1):
						row += row[n - 1 - abs(n-k)]
				else:
					if i + j <= n - 2:
						row += ' '
					elif ((i + j) - n) % 2 == 1:
						row += '-'
					elif ((i + j) - n) % 2 == 0:
						row += '|'
			ans += [row]
	return '\n'.join(ans)

for i in range(1,5):
	print '\n\ni: ', i
	print dashes(i)