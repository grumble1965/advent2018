#!/usr/bin/python3

from blist import blist

print('Hello advent - Day 9 - Problem 2')

def printBoard(player, circle, currentNdx):
	return
	str = '[{0}] '.format(player)
	for i in range(len(circle)):
		if i == currentNdx:
			str += '({0})'.format(circle[i])
		else:
			str += ' {0} '.format(circle[i])
	print(str)


def playGame(numPlayers, numMarbles):
	circle = blist([])
	currentNdx = -1

	scores = [0 for i in range(numPlayers)]

	# firstmarble
	circle.append(0)
	currentNdx = 0
	printBoard('-', circle, currentNdx)

	for marble in range(1, numMarbles+1):
		player = ((marble - 1) % numPlayers) + 1
		if not marble % 23 == 0:
			lo = (currentNdx + 1) % len(circle)
			hi = (currentNdx + 2) % len(circle)
			circle.insert(hi, marble)
			currentNdx = hi
			#while circle[0] != 0:
			#	tmp = circle[1:]
			#	tmp.append(circle[0])
			#	currentNdx = (currentNdx + len(circle) - 1) % len(circle)
			#	circle = tmp
		else:
			scores[player - 1] += marble
			takeNdx = (currentNdx + len(circle) - 7) % len(circle)
			scores[player - 1] += circle[takeNdx]
			del circle[takeNdx]
			currentNdx = takeNdx

		printBoard(player, circle, currentNdx)

	# find high score
	mx = -1
	for p in scores:
		if p > mx:
			mx = p

	return mx

linenum = 0
#with open('d9-test.txt') as f:
with open('d9-input.txt') as f:
	for line in f:
		words = line.split()
		numPlayers, numMarbles = int(words[0]), int(words[6])
		if len(words) == 12:
			highScore = int(words[11])
		else:
			highScore = -1
		print('play a game with', numPlayers, 'elves and', numMarbles, 'marbles', ('high score = '+str(highScore)) if highScore > 0 else '')
		linenum += 1

		finalScore = playGame(numPlayers, numMarbles*100)
		print('For', numMarbles*100, 'marbles, Final score is', finalScore)

print('read ', linenum, ' lines')
