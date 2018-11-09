#!/usr/bin/env python3

'''
Reference - 
https://www.coursera.org/lecture/algorithmic-toolbox/car-fueling-implementation-and-analysis-shwg1
https://www.coursera.org/lecture/algorithmic-toolbox/car-fueling-8nQK8
'''


def minStops(x,n,m):
	totalRefills = 0
	currentRefill = 0
	while currentRefill < n -1:
		lastRefill = currentRefill
		while currentRefill < n -1 and x[currentRefill+1] - x[lastRefill] <= m:
			currentRefill += 1
		if currentRefill == lastRefill:
			return False
		if currentRefill < n -1:
			totalRefills += 1
	return totalRefills
			

def main():
	x = [0, 200, 375, 550, 750, 950]
	m = 400
	n = len(x)
	print(minStops(x,n,m))
	pass

if __name__ == '__main__':
	main()

