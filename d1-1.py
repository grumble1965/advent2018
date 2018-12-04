#!/usr/bin/python3

print('Hello advent - Day 1 - Problem 1')

freq = 0

with open('d1-input.txt') as f:
	for line in f:
		change = int(line)
		freq += change

print('final calibration = ', freq)
