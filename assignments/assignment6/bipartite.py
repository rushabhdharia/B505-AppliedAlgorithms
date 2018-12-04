#!/usr/bin/env python3
dict_of_nodes = {} 

#We traverse through the whole adjacency list and check if any two neighbors have the same color. If any two neighbors have the same color then the graph is not bipartite, else it is bipartite.
def is_bipartite():
	for u in dict_of_nodes:
		for v in dict_of_nodes[u]['adjacency_list']:
			if dict_of_nodes[u]['color'] == dict_of_nodes[v]['color']:
				return 0
	return 1

# Normal DFS function with the only modification that it colors the node and it's predecessor with different colors.
def DFS():
	global dict_of_nodes
	color = "RED"
	stack = []

	for u in dict_of_nodes:
		if dict_of_nodes[u]['color'] == "WHITE":
			stack.append(u)

		while len(stack) != 0 :
			u = stack.pop()
			prev = dict_of_nodes[u]['pre'] 
			if prev != "NIL":
				if dict_of_nodes[prev]['color'] == "RED":
					color = "BLUE"
				else:
					color = "RED"
			dict_of_nodes[u]['color'] = color
			for v in dict_of_nodes[u]['adjacency_list']:
				if dict_of_nodes[v]['color'] == "WHITE":
					dict_of_nodes[v]['pre'] = u
					stack.append(v)

def main():
	global dict_of_nodes # to store all the nodes with their color, predecessor and neighbors

	#input file
	file = open("bipartite.txt") 
	# file = open("bipartite2.txt")
	# file = open("not_bipartite.txt")
	# file = open("not_bipartite2.txt")
	# file = open("test.txt")
	

	n = int(file.readline())

	# Read the file line by line 
	for line in file:
		check = 0 # to determine if its the first or second number
		num = line.split(',') 
		num1 = '' # stores the first node
		num2 = '' # stores the second node
		
		for y in num:
			for x in y:
				if x.isdigit():
					if check == 0:
						num1 += x
					else:
						num2 += x
			check += 1	

		a=int(num1)
		b=int(num2)


		# Check if a number is present in the dictionary. If it's not present add it to the dictionary and set its color to white, predecessor to NIL and make an empty neighbors list.
		if a not in dict_of_nodes:
			dict_of_nodes[a] = {}
			dict_of_nodes[a]['color'] = "WHITE"
			dict_of_nodes[a]['pre'] = "NIL"
			dict_of_nodes[a]['adjacency_list'] = []

		if b not in dict_of_nodes:
			dict_of_nodes[b] = {}
			dict_of_nodes[b]['color'] = "WHITE"
			dict_of_nodes[b]['pre'] = "NIL"
			dict_of_nodes[b]['adjacency_list'] = []

		# Add the other node to the node's neighbor list
		dict_of_nodes[a]['adjacency_list'].append(b)
		dict_of_nodes[b]['adjacency_list'].append(a)

	# Call the function to color the graph
	DFS()

	if is_bipartite():
		print("Graph is Bipartite")
	else:
		print("Graph is not Bipartite")
	pass

if __name__ == '__main__':
	main()