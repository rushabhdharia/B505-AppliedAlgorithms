#!/usr/bin/env python3
'''
Reference  -
http://www.cs.mun.ca/~kol/courses/3719-w12/scheduling.pdf
 
Sort the jobs so that: g1 ≥ g2 ≥ . . . ≥ gn
for t : 1..n
	S(t) ← 0 {Initialize array S(1), S(2), ..., S(n)}
end for
for i : 1..n
	Schedule job i in the latest possible free slot meeting its deadline;
	if there is no such slot, do not schedule i.
end for
'''
from collections import OrderedDict
import operator

def main():
	arr = [0, 0, 0, 0]
	job = {1:{'d':2, 'p':7}, 2:{'d':1, 'p':2}, 3:{'d':3, 'p':7}, 4:{'d':3, 'p':9}}
	sorted_job = OrderedDict(sorted(job.items(), key = lambda x: x[1]['p'], reverse = True))
	print(sorted_job)
	

	pass

if __name__ == '__main__':
	main()