#!/usr/bin/python3

print('Hello advent - Day 3 - Problem 2')

#size = 8
size = 1000
fabric = [[0 for x in range(size+1)] for y in range(size+1)]

goodclaims = set([])

linenum = 0
#with open('d3-test.txt') as f:
with open('d3-input.txt') as f:
	for line in f:
		linenum += 1

		# parse the line
		cl, _, start, size = line.split(' ')
		claim = int(cl.lstrip('#'))
		startx, starty = start.split(',')
		sx, sy = int(startx), int(starty.rstrip(':'))
		runx, runy = size.split('x')
		dx, dy = int(runx), int(runy)
		#print(claim, sx, sy, dx, dy)

		claimstodelete = set([])
		for x in range(sx, sx+dx):
			for y in range(sy, sy+dy):
				if not fabric[x][y] == 0:
					claimstodelete.add(fabric[x][y])
				fabric[x][y] = claim

		if len(claimstodelete) == 0:
			goodclaims.add(claim)
		else:
			goodclaims -= claimstodelete

print('read ', linenum, ' lines')
print('good claims: ', goodclaims)
