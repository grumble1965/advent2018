#!/usr/bin/python3

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# reduce a polymer string 
def reducePolymer( poly ):
	# find the letters used in the polymer
	used = set([])
	for cc in alphabet:
		if poly.find(cc.lower()) > -1:
			used.add(cc.lower())
		if poly.find(cc.upper()) > -1:
			used.add(cc.upper())
	# reduce a unit at a time until no changes
	done = False
	while not done:
		start = poly
		for ll in used:
			t1 = ll.lower() + ll.upper()
			tmp1 = poly.replace(t1, '', 1)
			t2 = t1.swapcase()
			poly = tmp1.replace(t2, '', 1)
		done = (len(poly) == len(start))
	return poly

print('Hello advent - Day 5 - Problem 2')

with open('d5-input.txt') as f:
	polymer = f.readline()
polymer = polymer.strip()

print('read polymer with', len(polymer), 'units')

results = []
for unit in alphabet:
	w = polymer.replace(unit.lower(), '')
	w = w.replace(unit.upper(), '')
	results.append(len(reducePolymer(w)))

print('Minimum polyer has length', min(results))
