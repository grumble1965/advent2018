#!/usr/bin/python3

print('Hello advent - Day 2 - Problem 2')

totalLines = 0
lines = []
with open('d2-input.txt') as f:
	for line in f:
		boxid = line.strip()
		totalLines += 1

		for prev in lines:
			matching = ""
			for ndx in range(len(prev)):
				if prev[ndx] == boxid[ndx]:
					matching += prev[ndx]
			if len(matching) == len(boxid)-1:
				print('matching substring = ', matching)
				exit(0)

		lines.append(boxid)

print('read ', totalLines, ' lines')
print('no match found')
