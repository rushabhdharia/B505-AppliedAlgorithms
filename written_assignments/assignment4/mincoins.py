#!/usr/bin/env python3

def main():
	change = [25, 10, 5, 1]
	money = 116
	list_of_change = []
	for i in change:
		while money>=i:
			money = money-i
			list_of_change.append(i)
	print(list_of_change)

	pass

if __name__ == '__main__':
	main()