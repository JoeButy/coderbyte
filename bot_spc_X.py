def launchSequenceChecker(systemNames, stepNumbers):
	names = set(systemNames)
	d = {}
	print d
	for i in range(len(stepNumbers)):
		if len(d[systemNames[i]]) == 0:
			print 'append: ', stepNumbers[i], 'TO:',  systemNames[i]
			print 'currently: ', d[systemNames[i]]
			d[systemNames[i]].append(stepNumbers[i])
			print 'FULL DICT', d
			print d[systemNames[i]]
		elif max(d[systemNames[i]]) < stepNumbers[i]:
			d[systemNames[i]].append(stepNumbers[i])
		else:
			print 'FAIL:', d[systemNames[i]]
			print d
			return False
	return True

m = ["stage_1", 
 "stage_2", 
 "dragon", 
 "stage_1", 
 "stage_2", 
 "dragon"]
s = [1, 10, 11, 2, 12, 111]
print '--**-- ' *8
print m
print s
print launchSequenceChecker(m, s)