#!/usr/bin/python3

print('Hello advent - Day 2 - Problem 1')

num2 = 0
num3 = 0
linenum = 0
with open('d2-input.txt') as f:
	for line in f:
		boxid = line.strip()
		linenum += 1

		letterDict = dict()
		for ch in boxid:
			if ch in letterDict:
				letterDict[ch] += 1
			else:
				letterDict[ch] = 1

		if 2 in letterDict.values():
			num2 += 1
		if 3 in letterDict.values():
			num3 += 1

checksum = num2 * num3
print('checksum = ', checksum)
print('read ', linenum, ' lines')
