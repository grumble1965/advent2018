#!/usr/bin/python3

print('Hello advent - Day 6 - Problem 1')

designations = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH', 'II', 'JJ', 'KK', 'LL', 'MM', 'NN', 'OO', 'PP', 'QQ', 'RR', 'SS', 'TT', 'UU', 'VV', 'WW', 'XX', 'YY', 'ZZ']

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

# find nearest marker 
for y in range(miny, maxy+1):
	for x in range(minx, maxx+1):
		if grid[y - miny][x - minx] == '.':
			distances = {}
			for (marker, (mx,my)) in points.items():
				distances[marker] = abs(mx - x) + abs(my - y)
			mindistance = min(distances.values())	
			scratch = []
			for (marker, dist) in distances.items():
				if dist == mindistance:
					scratch.append(marker)
			if len(scratch) == 1:
				grid[y - miny][x - minx] = scratch[0].lower()

# make a list of all possible markers, then remove infinte areas (these touch the edges)
possible = set(points.keys())
for x in range(minx, minx+1):
	t = grid[miny - miny][x - minx]
	possible.discard(t.upper())
	possible.discard(t.lower())
	b = grid[maxy - miny][x - minx]
	possible.discard(b.upper())
	possible.discard(b.lower())
for y in range(miny, maxy+1):
	l = grid[y - miny][minx - minx]
	possible.discard(l.upper())
	possible.discard(l.lower())
	r = grid[y - miny][maxx - minx]
	possible.discard(r.upper())
	possible.discard(r.lower())

# determine the size of each possible area
sizes = {}
for marker in possible:
	cnt = 0
	for y in range(miny, maxy+1):
		for x in range(minx, maxx+1):
			if grid[y-miny][x-minx] == marker.upper() or grid[y-miny][x-minx] == marker.lower():
				cnt += 1	
	sizes[marker] = cnt

maxsize = max(sizes.values())
for marker,size in sizes.items():
	if size == maxsize:
		print('largest region is ', marker, ' with size ', maxsize)

#for y in grid:
#	print(y)
