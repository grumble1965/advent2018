#!/usr/bin/python3

def setPrint(ss):
	string = ''
	for el in ss:
		string += el
	return string

print('Hello advent - Day 7 - Problem 2')

#numWorkers = 2
numWorkers = 5

steps = set([])
deps = set([])

cnt = 0
#with open('d7-test.txt') as f:
with open('d7-input.txt') as f:
	for line in f:
		tmp = line.split()
		s1, s2 = tmp[1], tmp[7]
		steps.add(s1)
		steps.add(s2)
		deps.add((s1, s2))
		cnt += 1

print('read', cnt, 'lines')
print('parsed', len(steps), 'steps and', len(deps), 'rules')

# given what's available, and dependencies, return possible next steps
def nextsteps(avail, depends):
	poss = set([])
	for target in steps:
		deps = set([])
		for (pp,qq) in depends:
			if qq == target:
				deps.add(pp)
		if deps <= avail:
			poss.add(target)
	return poss

# initial available steps are steps that don't appear as postconditions
initial = set([])
for ss in steps:
	hasDep = False
	for (pp,qq) in deps:
		if qq == ss:
			hasDep = True
	if not hasDep:
		initial.add(ss)


def printStat(time, workers, sequence):
	out = '{0}'.format(time)
	for (_, task) in workers:
		out += '   '
		out += '{0}'.format(task)
	print(out, '  ', sequence)

complete = set([])
inProgress = set([])
sequence = []

workers = [(-1, '.') for i in range(numWorkers)]

time = 0
while len(complete) < len(steps):
	# handle workers who are done
	for ndx in range(numWorkers):
		(togo, task) = workers[ndx]
		if togo == 0:
			# this task is complete
			inProgress.discard(task)
			complete.add(task)
			sequence.append(task)
			workers[ndx] = (-1, '.')

	# assign tasks to idle workers
	for ndx in range(numWorkers):
		(togo, task) = workers[ndx]
		if togo == -1 and task == '.':
			# find a task for this worker
			possibleNext = nextsteps(complete, deps)
			ss = (initial | possibleNext) - complete - inProgress
			if len(ss) > 0:
				nn = min(ss)
				workers[ndx] = (ord(nn)-ord('A') + 60, nn)
				inProgress.add(nn)
		elif togo > -1:
			# time goes by
			workers[ndx] = (togo-1, task)

	printStat(time, workers, sequence)
	time += 1

print('\nFinal sequence is: ', ''.join(sequence))
