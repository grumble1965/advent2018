#!/usr/bin/python3

print('Hello advent - Day 8 - Problem 1')

data = []
#with open('d8-test.txt') as f:
with open('d8-input.txt') as f:
	for line in f:
		for dd in line.split():
			data.append(dd)

print('read', len(data), 'words of data')

def parseTree():
	numNodes = int(data.pop(0))
	numMD = int(data.pop(0))

	nodes = []
	for nn in range(numNodes):
		nodes.append(parseTree())
	
	md = []
	for dd in range(numMD):
		md.append(int(data.pop(0)))

	return (nodes, md)

def sumMD(tree):
	sum = 0
	(nodes, md) = tree
	for n in nodes:
		sum += sumMD(n)
	for dd in md:
		sum += dd
	return sum

def valueNode(tree):
	value = 0
	(nodes, md) = tree
	if len(nodes) == 0:
		for dd in md:
			value += dd
	else:
		tmp = []
		for n in nodes:
			tmp.append(valueNode(n))
		for dd in md:
			if dd-1 in range(len(tmp)):
				value += tmp[dd-1]
	return value

root = parseTree() 
mdSum = sumMD(root)
val = valueNode(root)

print('Sum of metadata =', mdSum)
print('Value of tree =', val)
