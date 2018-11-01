#!/usr/bin/env python3
from string import ascii_lowercase
import heapq
#from queue import PriorityQueue

def traverseTree(node, bit):
	if node.left is null and node.right is null:	# if this is leaf node
		print node.char, bit			# print code (or save it somewhere else)
	else:
		traverseTree(node.left, bit + '0')	# stick a 0 to the bit and continue down left
		traverseTree(node.right, bit + '1')	# stick a 1 to the bit and continue down right

def main():
	chardict = {}
	char_list = []

	for character in ascii_lowercase:
		char_list.append(character)

	char_list.append(' ')
	char_list.append('.')
	char_list.append(',')
	char_list.append('!')
	char_list.append('?')
	char_list.append('\'')

	for character in char_list:
		chardict[character] = 0

	print(chardict)
	#print(char_list)

	file = open("The Adventures of Sherlock Holmes.txt")
	while True:
		c = file.read(1)
		if not c:
			break
		if c in char_list:
			chardict[c] += 1	
	file.close()
	print(chardict)	

	# Q = PriorityQueue()
	# for c in char_list:
	# 	Q.put(chardict[c], c)

	# while Q.qsize()>0:
	# 	print(Q.get())

	Q = []					# create empty queue
	for c in char_list:				# for each character c in your character set:
		heapq.heappush(Q, (chardict[c], c))	# push tuple of "(frequency, char)" onto queue, so that they get keyed on the frequency

	while len(Q)>0:
		print(heapq.heappop(Q))

	pass

if __name__ == '__main__':
	main()