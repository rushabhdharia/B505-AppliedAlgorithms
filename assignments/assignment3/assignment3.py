#!/usr/bin/env python3

import math
import sys
import time
import matplotlib.pyplot as plt
import random

#-----------------------------------------------
# Reference 1 - CLRS pg 34
# Reference 2 - https://www.geeksforgeeks.org/merge-sort/ 

def merge(A, beg, mid, end):
	n1 = mid - beg + 1
	n2 = end - mid

	L=[0 for _ in range(n1)]
	R=[0 for _ in range(n2)]

	for i in range(0,n1):
		L[i]=A[beg+i]

	for j in range(0,n2):
		R[j] = A[mid+j+1]

	i=0
	j=0
	k = beg

	while (i<n1 and j<n2):
		if (L[i] <= R[j]):
			A[k] = L[i]
			i=i+1
		else:
			A[k] = R[j]
			j+=1
		k+=1
	
	while (i < n1): 
		A[k] = L[i] 
		i += 1
		k += 1
  
	while (j < n2): 
		A[k] = R[j] 
		j += 1
		k += 1

	return    

def mergeSort(A,beg,end):
	if(beg<end):
		mid = (beg+end)//2
		mergeSort(A, beg, mid)
		mergeSort(A, mid+1, end)
		merge(A, beg, mid, end)
	return

#------------------------------------------------------	

def plot_graph(time):
	no_of_inputs = []
	i = 5000
	while(i<=100000):
		no_of_inputs.append(i)
		i+=5000
	plt.plot(no_of_inputs,time)
	plt.xlabel('no of inputs')
	plt.ylabel('time')
	plt.show()


def call_to_mergesort():
	file = open("input.txt","r")
	n = 5000
	time1 = []
	string_Numbers = file.read().splitlines()
	while(n<=100000):
		avg_time = 0
		for i in range(0,3):
			a = []
			a = list(map(int, string_Numbers[:n])) #https://stackoverflow.com/questions/7368789/convert-all-strings-in-a-list-to-int
			start = time.time()
			mergeSort(a,0,n-1)
			end = time.time()
			total_time = end - start
			avg_time += total_time
		avg_time=avg_time/3 
		time1.append(avg_time)
		n+=5000 
	print(time1)
	plot_graph(time1)
	file.close()


#--------------------------------------
#Reference CLRS pg 18 
def insertion_sort(A):
	for j in range(1, len(A)):
		key = A[j]
		i = j-1
		while (i>=0 and A[i]>key):
			A[i+1] = A[i]
			i = i-1
		A[i+1] = key
#-----------------------------------------

def get_median(A):
	n = len(A)
	return A[n//2]

#----------------------------------------------------------------------------------
#Reference - https://github.com/tatiana/algorithms/blob/master/algorithms/utils.py
def split_list_by_pivot(A, pivot):
	smaller = []
	larger = []
	for value in A:
		if value < pivot:
			smaller.append(value)
		elif value > pivot:
			larger.append(value)
	return smaller, larger

#-------------------------------------------------------------------------------------	

def select(A, k):
	n = len(A)
	if (n <= 5):
		insertion_sort(A)
		k = int(k)
		return A[k - 1]

	a = math.ceil(n/5)
	B = [[] for _ in range (a)]

	counter = 0
	count = 0

	for i in range(n):
		B[counter].append(A[i])
		count+=1
		if (count==5):
			count = 0
			counter+=1

	medians_list = []

	for chunk in B:
		insertion_sort(chunk)
		medians_list.append(get_median(chunk))

#----------------------------------------------------------------------------------
#Reference - https://github.com/tatiana/algorithms/blob/master/algorithms/selection.py
	size = len(medians_list)
	mom = select(medians_list, size / 2 + (size % 2))
	smaller, larger = split_list_by_pivot(A, mom)
	values_before_mom = len(smaller)

	if values_before_mom == (k - 1):
		return mom
	elif values_before_mom > (k - 1):
		return select(smaller, k)
	else:
		return select(larger, k - values_before_mom - 1)
#-------------------------------------------------------------------------------------	



def call_to_select():
	#smaller array
	A = [13, -3, -25, -16, -23, 18, 20, -7, 12, -5, -22, 15]

	#random array of 50 elements 
	#A = random.sample(range(-100,100), 50)
	#print(A)

	#larger array of 50 elements
	#A = [-18, -34, 55, -2, -72, 26, 75, 23, -22, 21, -59, 31, 72, 50, -68, 70, -27, -61, 76, 88, 63, -55, -66, 42, 39, 91, 25, -12, -5, 80, -24, -39, -4, -38, 74, -82, -11, 5, -87, 57, 47, -32, 4, 56, 2, -28, -49, -91, 22, -21]
	
	i = 10		#ith smallest element
	ith_element = select(A,i)
	print ("The", i, "th element is :", ith_element)

def main():
	print("Press 1 for MergeSort")
	print("Press 2 for Select")
	key = input("Select an option:")
	if(key == "1"):
		call_to_mergesort()
	elif(key == "2"):
		call_to_select()
	else:
		("Wrong input. Please enter Option 1 or 2")

if __name__ == '__main__':
	main()