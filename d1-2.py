#!/usr/bin/python3

print('Hello advent - Day 1 - Problem 2')

freq = 0
history = {0}
found = False

while not found:
	with open('d1-input.txt') as f:
		for line in f:
			change = int(line)
			freq += change
			if freq in history:
				found = True
				break
			else:
				history.add(freq)
	print('looping...')

print('duplicate value = ', freq)
