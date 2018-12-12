#!/usr/bin/python3

print('Hello advent - Day 11 - Problem 1')

def calcPowerLevel(x, y, serial):
	rackID = x + 10
	pl = rackID * y
	pl += serial
	pl *= rackID
	pl = (pl // 100) % 10
	pl -= 5
	return pl

# testing
print('Power level @(  3,   5) # 8:', calcPowerLevel(3, 5, 8))
print('Power level @(122,  79) #57:', calcPowerLevel(122, 79, 57))
print('Power level @(217, 196) #39:', calcPowerLevel(217, 196, 39))
print('Power level @(101, 153) #71:', calcPowerLevel(101, 153, 71))

# fill in grid values
grid = [[0 for _ in range(300)] for _ in range(300)]
serial = 8561
for y in range(1, 300):
	for x in range(1, 300):
		grid[y-1][x-1] = calcPowerLevel(x, y, serial)

# compute 3x3 grid sums
sums = [[0 for _ in range(297)] for _ in range(297)]
for y in range(1, 297):
	for x in range(1, 297):
		s =   grid[y-1][x-1] + grid[y-1][x] + grid[y-1][x+1] + grid[y][x-1]   + grid[y][x]   + grid[y][x+1] + grid[y+1][x-1] + grid[y+1][x] + grid[y+1][x+1]
		sums[y-1][x-1] = s

# find maximum sum
maxsum, mx, my = float('-inf'), -1, -1
for y in range(1, 297):
	for x in range(1, 297):
		if sums[y-1][x-1] > maxsum:
			maxsum, mx, my = sums[y-1][x-1], x, y
			

print('max sum =', maxsum,'at (', mx, ',', my, ')')
