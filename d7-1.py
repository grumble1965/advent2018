#!/usr/bin/python3

def setPrint(ss):
	string = ''
	for el in ss:
		string += el
	return string

print('Hello advent - Day 7 - Problem 1')

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

complete = set([])
incomplete = steps
sequence = []

while len(complete) < len(steps):
	possibleNext = nextsteps(complete, deps)
	ss = (initial | possibleNext) - complete
	nn = min(ss)
	complete.add(nn)
	sequence.append(nn)

print('\nFinal sequence is: ', ''.join(sequence))
