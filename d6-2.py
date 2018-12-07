#!/usr/bin/python3

print('Hello advent - Day 6 - Problem 1')

designations = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH', 'II', 'JJ', 'KK', 'LL', 'MM', 'NN', 'OO', 'PP', 'QQ', 'RR', 'SS', 'TT', 'UU', 'VV', 'WW', 'XX', 'YY', 'ZZ']

#cutoff = 32
cutoff = 10000

points = {}
cnt = 0
#with open('d6-test.txt') as f:
with open('d6-input.txt') as f:
	for line in f:
		rx, ry = line.split(',')
		x, y = int(rx), int(ry)
		marker = designations[cnt]
		points[marker] = (x,y)
		cnt += 1

print('read', cnt, 'lines')

# find the extents
minx, miny, maxx, maxy = 99999, 99999, -1, -1
for (x,y) in points.values():
	minx = x if x < minx else minx
	miny = y if y < miny else miny
	maxx = x if x > maxx else maxx
	maxy = y if y > maxy else maxy
#print('minimum = (', minx, ',', miny, ') maximum = (', maxx, ',', maxy, ')')

# make a grid
grid = [['.' for x in range(minx,maxx+1)] for y in range(miny, maxy+1)]
for (marker, (x,y)) in points.items():
	grid[y - miny][x - minx] = marker

# for each location, compute distance to all markers
size = 0
for y in range(miny, maxy+1):
	for x in range(minx, maxx+1):
		dist = 0
		for (marker, (mx,my)) in points.items():
			dist += abs(mx - x) + abs(my - y)
		if dist < cutoff:
			grid[y - miny][x - minx] = '#'
			size += 1

print('size of region is ', size)

#for y in grid:
#	print(y)
