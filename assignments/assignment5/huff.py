#!/usr/bin/env python3
from string import ascii_lowercase
import heapq

globaldict = {}

class Node:
	def __init__(self):
		self.left = None
		self.right = None
		self.freq = None
		pass

	def __lt__(self, other):
		return self.freq < other.freq  #given that self.freq contains the frequency of your character

def traverseTree(node, bit):
	global globaldict
	if node[1].left is None and node[1].right is None:	# if this is leaf node
		globaldict[node[1].char] = bit
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
		new_node.freq = freq
		heapq.heappush(Q, (freq, new_node))

	return heapq.heappop(Q)


def main():
	global globaldict
	chardict = {}
	char_list = []
	total_char = 0
	no_of_bits = 0
	total_length = 0

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

	file = open("The Adventures of Sherlock Holmes.txt")
	#file = open("test.txt")
	while True:
		c = file.read(1)
		if not c:
			break
		if c in char_list:
			chardict[c] += 1
			total_char += 1	
	file.close()	

	Q = []					# create empty queue
	for c in char_list:			# for each character c in your character set:
		my_node = Node()		# create new node
		my_node.char = c		# assign c to char attribute of the node
		my_node.freq = chardict[c]
		heapq.heappush(Q, (chardict[c], my_node))	# push tuple of "(frequency, node)" onto queue, so that they get keyed on the frequency	
	
			
	node1 =	huffman(Q)
	traverseTree(node1, "")

	for key in globaldict.keys():
		length = len(globaldict[key])
		no_of_bits += length*chardict[key]

	total_length = 5*total_char
	saved_bits = total_length - no_of_bits
	print()
	print("The text was encoded using", no_of_bits,"bits")
	print("The text had", total_char, "valid characters")
	print("Using a 5-bit fixed length encoding, this would have been", total_length, "long")
	print("So we saved", saved_bits,"bits!")

	pass

if __name__ == '__main__':
	main()

