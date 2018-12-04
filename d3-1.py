#!/usr/bin/python3

print('Hello advent - Day 3 - Problem 1')

size = 1000
fabric = [[0 for x in range(size+1)] for y in range(size+1)]

linenum = 0
with open('d3-input.txt') as f:
	for line in f:
		linenum += 1

		cl, _, start, size = line.split(' ')
		claim = int(cl.lstrip('#'))
		startx, starty = start.split(',')
		sx, sy = int(startx), int(starty.rstrip(':'))
		runx, runy = size.split('x')
		dx, dy = int(runx), int(runy)
		#print(claim, sx, sy, dx, dy)

		for x in range(sx, sx+dx):
			for y in range(sy, sy+dy):
				fabric[x][y] += 1	

print('read ', linenum, ' lines')

conflicts = 0
for row in fabric:
	for element in row:
		if element > 1:
			conflicts += 1
print('found ', conflicts, ' conflicts')
