#!/usr/bin/env python3
from string import ascii_lowercase
import heapq

class Node:
	def __init__(self):
		self.left = None
		self.right = None
		self.freq = None
		pass

	#def __lt__(self, other):
	#	return self.freq < other.freq  #given that self.freq contains the frequency of your character

def traverseTree(node, bit):
	#print("here")
	if node[1].left is None and node[1].right is None:	# if this is leaf node
		print (node[1].char, bit)			# print code (or save it somewhere else)
	else:
		traverseTree(node[1].left, bit + '0')	# stick a 0 to the bit and continue down left
		traverseTree(node[1].right, bit + '1')	# stick a 1 to the bit and continue down right

def huffman(Q):
	while len(Q)>1:
		new_node = Node()
		new_node.left = x = heapq.heappop(Q)
		new_node.right = y = heapq.heappop(Q)
		freq = x[0] + y[0]
		heapq.heappush(Q, (freq, new_node))

	return heapq.heappop(Q)


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

	Q = []					# create empty queue
	for c in char_list:			# for each character c in your character set:
		my_node = Node()		# create new node
		my_node.char = c		# assign c to char attribute of the node
		my_node.freq = chardict[c]
		heapq.heappush(Q, (chardict[c], my_node))	# push tuple of "(frequency, node)" onto queue, so that they get keyed on the frequency	
	
			
	node1 =	huffman(Q)
	traverseTree(node1, "")
	pass

if __name__ == '__main__':
	main()