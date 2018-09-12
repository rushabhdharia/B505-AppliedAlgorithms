#!/usr/bin/python3
#Assignment 1
#Rushabh Ashok Dharia 
import time
import matplotlib.pyplot as plt

def bubbleSort(a,n):
	#Bubble Sort Algo
	# Introduction to Algorithms(CLRS) Edition 3 pg 40
	start = time.time()
	for i in range (0,n-1):
		j=n-1;
		while(j>i):
			j-=1
			if a[j]>a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]

	end = time.time()
	return end-start

def plot_graph(time):
	no_of_inputs = []
	i = 500
	while(i<=10000):
		no_of_inputs.append(i)
		i+=500
	plt.plot(no_of_inputs,time)
	plt.xlabel('no of inputs')
	plt.ylabel('time')
	plt.show()

def main():
	file = open("input.txt","r")
	n = 500
	time = []
	string_Numbers = file.read().splitlines()
	while(n<=10000):
		avg_time = 0
		for i in range(0,3):
			a = []
			a = list(map(int, string_Numbers[:n])) #https://stackoverflow.com/questions/7368789/convert-all-strings-in-a-list-to-int
			avg_time += bubbleSort(a,n)
		avg_time=avg_time/3	
		time.append(avg_time)
		n+=500	
	print(time)
	plot_graph(time)
	file.close()

if __name__ == "__main__":
	main()


#Another Implementation - https://www.geeksforgeeks.org/bubble-sort/
#for i in range (0,n-1):
#	for j in range(0, n-i-1):
#		if a[j]>a[j+1]:			
#a[j], a[j+1] = a[j+1], a[j]