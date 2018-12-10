#!/usr/bin/python3

print('Hello advent - Day 10 - Problem 1')

stars = []

linenum = 0
#with open('d10-test.txt') as f:
with open('d10-input.txt') as f:
	for line in f:
		startPos = line.find('<') + 1
		endPos = line.find('>')
		pos = line[startPos:endPos].split(',')

		startVel = line.find('<', startPos + 1) + 1
		endVel = line.find('>', endPos + 1)
		vel = line[startVel:endVel].split(',')

		position = (int(pos[0]), int(pos[1]))
		velocity = (int(vel[0]), int(vel[1]))
		stars.append( (position, velocity) )

		linenum += 1

print('read ', linenum, ' lines')

def timeStep(oldStars):
	newStars = []
	for ss in oldStars:
		((x, y), (dx, dy)) = ss
		newStars.append(((x+dx, y+dy), (dx, dy)))	
	return newStars
			
def displayStars(starField, time):
	offsetx, offsety = 150, 100
	buff = [ [' ' for x in range(80)] for y in range(25) ]
	for ss in starField:
		((x,y), _) = ss
		if x in range(offsetx, offsetx+80) and y in range(offsety, offsety+25):
			buff[y-offsety][x-offsetx] = '#'	
	print('\nTime =', time)
	for ll in buff:
		print(''.join(ll))

def starStats(starField):
	cnt, sumx, sumy = 0, 0, 0
	minx, miny, maxx, maxy = float('inf'), float('inf'), float('-inf'), float('-inf')
	for ss in starField:
		((x,y), _) = ss
		sumx, sumy = sumx + x, sumy + y
		if x < minx:
			minx = x
		if x > maxx:
			maxx = x
		if y < miny:
			miny = y
		if y > maxy:
			maxy = y
		cnt += 1
	return ((int(sumx / cnt), int(sumy / cnt)), (minx, miny), (maxx, maxy))

def displayStats(stats):
	(center, (minx, miny), (maxx, maxy)) = stats
	minp = (minx, miny)
	maxp = (maxx, maxy)
	extent = (abs(maxx-minx) + abs(maxy-miny))
	print(center, minp, maxp, extent)	

starSize = {}

# displayStars(stars, 0)
for t in range(50000):
	stars = timeStep(stars)
	(_, (minx, miny), (maxx, maxy)) = starStats(stars)
	starSize[t] = abs(maxx-minx) + abs(maxy-miny)
	if (abs(t-10311) < 5):
		displayStats(starStats(stars))
		displayStars(stars, t+1)

minSize = float('inf')
minTime = -1
for (t, s) in starSize.items():
	if s < minSize:
		minSize, minTime = s, t

print('smallest size was', minSize, 'at time', minTime)
