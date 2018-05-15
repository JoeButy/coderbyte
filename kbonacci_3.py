import time
start_time = time.time()

t = 10**5

def kfib(k, n):
	n += 1
	v = [1] * k
	if n < k:
		print n, k
		return 1
	else:
		for i in range(k, n):
			c = sum(v)
			v.append(c)
			v = v[1:]
			print v, c
		return v[-1]

def kbonacci(k, n):
	return str(kfib(k,n))

# Driver Program

test_set = [[3,4,'5'], [2,4,'5'], [2,0,'1'], [5,0,'1'], [5, 5,'5'], [30, 1000, '289396718207307436036942790598319910496422071412701662422240606584901117716101970863077372638217908819527416486433194886070733664434656467319129395485343853897457899729692875675064457796337224458570227273640202571309237214035797613779008748465939907306492719357080951631167768886130731683397633']]
# test_set = range(2, 10, 1)

def kbonacci(k, n):
    seq = []
    for i in range(1, n + 2):
        if i <= k:
            val = 1
        else:
            val = sum(seq[i-k-1:i-1])
        seq.append(val)
    return str(seq[-1])

for s in test_set:
# 	print '\nK:', s
	y = kbonacci(s[0], s[1])
	print s, ':', y, '==', s[2], y == s[2]
time2 = time.time()
print time2 - start_time

for s in test_set:
# 	print '\nK:', s
	y = kbonacci(s[0], s[1])
	print s, ':', y, '==', s[2], y == s[2]
print time.time() - time2

