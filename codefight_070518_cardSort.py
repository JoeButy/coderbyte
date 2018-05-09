def maxCardSequence(cards):
	cards.sort()
	dk = []
	dk.append(cards[0])
	for j in range(len(cards)):
		if (cards[j] > dk[-1]) & (cards[j] % 2 != dk[-1] % 2):
			dk.append(cards[j])
		else:
			pass
	return len(dk)

test_set = [[3, 2, 8, 1, 4, 3], [1], [2], [100, 27, 14]]

for k in test_set:
	print k, maxCardSequence(k)
