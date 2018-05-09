import math

test_set = \
	[[251129265,673395586],
	[105198459,805822999],
	[717757366,213356038],
	[138127119,369545330],
	[190352610,593431801],
	[826921131,48669151],
	[725660770,667662425],
	[380307315,524023846],
	[121041130,750161545],
	[855757028,879543000]]

ans=[1,1,0,1,1,1,1,0,1,0]
print '--+'*12
def bi(x):
	return '{0:b}'.format(x)
def count_z(a):
	return a.count('0'), a.count('1')

def fifth_bit(a):
	return bi(a)[len(bi(a))-6]

for i, pair in enumerate(test_set):
	a = pair[0]
	b = pair[1]
	c = pow(a,2) + pow(b,2)
	bc = bi(c)
	print bc, fifth_bit(c), ans[i]
	print pair, ' -- Answer: ', ans[i]
	print a, bi(a), count_z(bi(a)), fifth_bit(a)#, ' isPrime:', isPrime(a)
	print b, bi(b), count_z(bi(b)), fifth_bit(b)#, ' isPrime:', isPrime(b)
	
	print ans[i]
# 	print a%b, a<b
# 	print b%a, b<a
# 	print min(a%b, b%a), 'mod'
# 	print 'a mod 2 == b mod 2', a%2==b%2
# 	print 'Greatest Common Denominator:', gcd(a, b)

# 	print 'subtacted even or odd', (a-b)
	
	print '\n'
	
# 
# def gcd(a, b):
# 	ls = []
# 	count = 0
# 	while b:
# 		if isPrime(a) or isPrime(b):
# 			print count, ':', a, b
# 			count += 1
# 		a, b = b, a%b
# # 		print '2:', a, b
# 	return a
# 
# def isPrime(n):
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
# 
#     return True
# 
