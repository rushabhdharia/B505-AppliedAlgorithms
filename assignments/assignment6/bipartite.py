#!/usr/bin/env python3
import math
dict_of_nodes = {} 

def is_bipartite(G):
	for u in range(len(G)):
		for v in G[u]:
			if dict_of_nodes[u+1]['color'] == dict_of_nodes[v]['color']:
				return 0
	return 1

def DFS(G):
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
			for v in G[u-1]:
				if dict_of_nodes[v]['color'] == "WHITE":
					dict_of_nodes[v]['pre'] = u
					stack.append(v)

def main():
	global dict_of_nodes

	file = open("bipartite.txt")
	# file = open("bipartite2.txt")
	# file = open("not_bipartite.txt")
	# file = open("not_bipartite2.txt")
	
	adjacency_list = []
	n = int(file.readline())
	
	for i in range(0,n):
		adjacency_list.append([])
		x = i+1
		dict_of_nodes[x] = {}
		dict_of_nodes[x]['color'] = "WHITE"
		dict_of_nodes[x]['pre'] = "NIL"

	for line in file:
		check = 0
		
		for x in line:
			if x.isdigit():
				if check == 0:
					a = int(x)
				else:
					b = int(x)
				check += 1	

		adjacency_list[a-1].append(b)
		adjacency_list[b-1].append(a)

	DFS(adjacency_list)

	if is_bipartite(adjacency_list):
		print("Graph is Bipartite")
	else:
		print("Graph is not Bipartite")
	pass

if __name__ == '__main__':
	main()