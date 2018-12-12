#!/usr/bin/python3

print('Hello advent - Day 11 - Problem 2')

def calcPowerLevel(x, y, serial):
	rackID = x + 10
	pl = rackID * y
	pl += serial
	pl *= rackID
	pl = (pl // 100) % 10
	pl -= 5
	return pl

# testing
#print('Power level @(  3,   5) # 8:', calcPowerLevel(3, 5, 8))
#print('Power level @(122,  79) #57:', calcPowerLevel(122, 79, 57))
#print('Power level @(217, 196) #39:', calcPowerLevel(217, 196, 39))
#print('Power level @(101, 153) #71:', calcPowerLevel(101, 153, 71))

def printGrid(array):
	for y in array:
		for element in y:
			print("{0:3d}".format(element), end=' ')
		print()

# global configuration
#serial = 18
#serial = 42
serial = 8561

#gridSize = 10
gridSize = 300

# fill in grid values
grid = [[0 for _ in range(gridSize)] for _ in range(gridSize)]
for y in range(1, gridSize):
	for x in range(1, gridSize):
		grid[y-1][x-1] = calcPowerLevel(x, y, serial)
#printGrid(grid)

maxsum, mx, my, msize = float('-inf'), -1, -1, -1

# compute sizeXsize grid sums
for size in range(1,gridSize+1):
	#print()
	print('size =', size)
	if size < 2:
		oldSums = grid
		sums = grid
	else:
		oldSums = sums
		sums = [[0 for _ in range(gridSize-size+1)] for _ in range(gridSize-size+1)]
		for y in range(1, gridSize-size+2):
			for x in range(1, gridSize-size+2):
				s = oldSums[y - 1][x - 1]
				#print('s = oldSums[', x-1, ',', y-1, ']', end='')
				for yy in range(y, y + size):
					s += grid[yy - 1][x + size - 2]
					#print('+ grid[', x+size-2, ',', yy-1, ']', end='')
				for xx in range(x, x + size):
					s += grid[y + size - 2][xx - 1]
					#print('+ grid[', xx-1, ',', y+size-2, ']', end='')
				s -= grid[y + size - 2][x + size - 2]
				#print(' - grid[', x+size-2, ',', y+size-2, ']')
				sums[y - 1][x - 1] = s

				# find maximum sum
				if sums[y-1][x-1] > maxsum:
					maxsum, mx, my, msize = sums[y-1][x-1], x, y, size
			
	#printGrid(sums)

print('max sum =', maxsum,'at (', mx, ',', my, ') in grid size', msize)
