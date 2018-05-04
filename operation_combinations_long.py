import itertools as it
import random
'''
Code Fight Daily Challenge 5/3/2018:

Special thanks to @kov for this 237 idea. Here is our problem today.

Provided 5 integers a, b, c, d, e as an array and 4 basic arithmetic operations + - * /. Your mission is to identify and count all the equations that have results ended up in 237 following the below rules:

You must use all 5 integers in the equation;
You can have duplicated operations like a * b * c * d * e;
In case a = b, equation a + b + c + d + e is different from b + a + c + d + e. You must count both. (ie.: [1, 1, 2, 3, 4])
Example
For arr = [79, 0, 1, 3, 5], the output should be
int237(arr) = 186.
a = 79, b = 0, c = 1, d = 3, e = 5
You can have a list of following equations that ended up in 237:

0 * 1 * 5 + 3 * 79 = 237
0 * 1 * 5 + 79 * 3 = 237
0 * 1 / 5 + 3 * 79 = 237
... and so on
There are 186 equations that equal to 237. Thus the final answer is 186

Input/Output

[execution time limit] 4 seconds (py)

[input] array.integer arr

Guaranteed constraints:
arr.length = 5,
0 <= arr[i] <= 237.

[output] integer
'''

num_inputs = 5
op_list = ['/', '*', '+', '-']
op_perms = [p for p in it.product(op_list, repeat=num_inputs-1)]
target = 237


def eval_function(x, op):
	'''this function zips a list of floats and operations placing the operators in between 
	the integers. There must be on less on more integer in list x than operators in list op.
	The value is evaluated and compared to the target value.'''
	eval_str = ''
	div_limit = False
	for i in range(0,4):
# 		print i, x[i], op[i]
		eval_str = eval_str + str(x[i]) + op[i]
# 		print eval_str
	eval_str = eval_str + str(x[num_inputs - 1])
	try:
		tot = eval(eval_str)
	except ZeroDivisionError:
		tot = False
	result = tot == target
	return result
	

def int237(arr):
	'''with the input arr, create all the permutations of that set and for each one, use the
	cartesian product of operators to evaluate the number of ways the arr can be combine
	to hit a target value.'''
	x_perms = [p for p in it.permutations(arr, num_inputs)]
	total_hits = 0
	for x_perm in x_perms:
		input = [float(i) for i in x_perm]
		for op_perm in op_perms:
			if eval_function(input, op_perm):
				total_hits += 1
			else:
				pass
	return total_hits

## create random sample data to test!
# print results
for i in range(100):
	test_set = random.sample(range(0, target), num_inputs)
	print test_set, int237(test_set)
print [79,0,1,3,5], int237([79,0,1,3,5])