#!/usr/bin/python3

print('Hello advent - Day 4 - Problem 1')

with open('d4-input.txt') as f:
	lines = f.readlines()
lines.sort()

sleepTimes = dict([])
guard = -1
awakeTime = -1
for logline in lines:
	# parse minute (now), guard number, line type
	ww = logline.split(' ')
	_, mm = ww[1].rstrip(']').split(':')
	minute = int(mm)
	uu = ww[2]

	if uu == 'Guard':
		guard = int(ww[3].lstrip('#'))
		if guard not in sleepTimes:
			sleepTimes[guard] = [0 for ii in range(60)]
		awakeTime = 0
	elif uu == 'falls':
		sleepTime = minute
	elif uu == 'wakes':
		for ii in range(sleepTime, minute):
			sleepTimes[guard][ii] += 1
	else:
		print('oops')

# find guard with highest sleep total
guard, maxsleep = -1, -1
for gg in sleepTimes.keys():
	total = 0
	for ii in sleepTimes[gg]:
		total += ii
	if total > maxsleep:
		guard, maxsleep = gg, total
print('sleepiest guard ', guard)

# for that guard, find minute most spent asleep
mm = max(sleepTimes[guard])
tt = sleepTimes[guard].index(mm)
print('commonly asleep at ', tt)

# compute guard * minute
print('answer is: ', guard * tt)
print('read ', len(lines), ' lines')
