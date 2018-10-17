#!/usr/bin/env python3
#Assignment 2
#Rushabh Ashok Dharia 
import time
import matplotlib.pyplot as plt
import copy
import math

# Complexity n^2
def bruteforce2(A,n):
	highestsum = -10000 #infinity	#stores the largest sum	
	sumOfArr = 0					#stores the sum of the sub array in consideration
	sub_arr = []					#stores all the indices of the sub array
	start = time.time()
	#--------------------------------------------------------------------------------------------
	#https://stackoverflow.com/questions/41904746/why-is-the-maximum-sum-subarray-brute-force-on2
	for i in range(0,n):
		sumOfArr = 0	
		temp_arr = []	
		for j in range(i,n):
			sumOfArr += A[j]
			temp_arr.append(j)						
			if(highestsum<sumOfArr):
				sub_arr = copy.deepcopy(temp_arr)
				highestsum = sumOfArr
	#--------------------------------------------------------------------------------------------
	end = time.time()
	total_time = end - start 	
	n = len(sub_arr)		
	return sub_arr[0], sub_arr[n-1], highestsum, total_time		

# Another Method 
# Complexity n^3
# def bruteforce3(A,n): 
# 	highestsum = -10000 #infinity	#stores the highest sum
# 	sumOfArr = 0	#stores the sum of current sub array
# 	sub_arr = []
# 	temp_arr = []
# 	temp_arr_index = []
# 	start = time.time()
# 	for i in range(1,n+1):
# 		counter = 0		
# 		for j in range(n):
# 			for k in range(counter,counter+i):
# 				if(k<n):
# 					sumOfArr += A[k]
# 					temp_arr.append(k)	
# 					temp_arr_index.append(k)				
# 			if(highestsum<sumOfArr):
# 				sub_arr = temp_arr
# 				highestsum = sumOfArr
# 			temp_arr = []
# 			sumOfArr = 0
# 			counter+=1
# 			if((counter+i)>n):
# 				break
# 	end = time.time()
# 	total_time = end - start
# 	n = len(sub_arr)			
# 	return  sub_arr[0], sub_arr[n-1],highestsum, total_time

# CLRS pg 71 -----------------------------------------------------------------------------
def findMaxCrossingSubArray(A, low, mid, high):
	left_sum = -10000 # -infinity
	sum = 0
	for i  in range(mid, low-1, -1):
		sum = sum + A[i]
		if sum>left_sum:
			left_sum = sum
			max_left = i
	right_sum = - 10000 # -infinity
	sum = 0
	for j in range (mid+1, high+1):
		sum = sum + A[j]
		if sum>right_sum:
			right_sum = sum
			max_right=j
	return (max_left, max_right, left_sum+right_sum)

def findMaxSubArray(A,low,high):
	if (high==low):
		return (low, high, A[low])
	else:
		mid = (low+high)//2
		left_low, left_high,left_sum = findMaxSubArray(A,low,mid)
		right_low, right_high, right_sum = findMaxSubArray(A, mid+1, high)
		cross_low, cross_high, cross_sum = findMaxCrossingSubArray(A, low, mid, high)
		if(left_sum>=right_sum and left_sum>=cross_sum):
			return (left_low, left_high,left_sum)
		elif(right_sum>=left_sum and right_sum>=cross_sum):
			return (right_low, right_high, right_sum)
		else:
			return (cross_low, cross_high, cross_sum)			
#----------------------------------------------------------------------------------------

def plot_graph(time1, time2):
	no_of_inputs = []
	i = 500
	while(i<=10000):
		no_of_inputs.append(i)
		i+=500
	plt.plot(no_of_inputs,time1, 'r', label = "Brute Force")
	plt.plot(no_of_inputs,time2, 'b', label = "Divide and Conquer")
	plt.xlabel('no of inputs')
	plt.ylabel('time')
	plt.legend()
	plt.show()

def main():	
	file = open("input.txt","r")
	n = 500
	time1 = []
	time2 = []
	string_Numbers = file.read().splitlines()
	A = list(map(int, string_Numbers[:n]))

	# low,high,sub_sum,total_time = bruteforce2(A,n)
	# print( "max subrray = A["+str(low)+".."+str(high)+"]")
	# print("Max Sum = "+str(sub_sum))

	# low,high,sub_sum = findMaxSubArray(A,0,n-1)
	# print( "max subrray = A["+str(low)+".."+str(high)+"]")
	# print("Max Sum = "+str(sub_sum))

	while(n<=10000):
		avg_time = 0
		for i in range(0,3):
			A = []
			A = list(map(int, string_Numbers[:n])) #https://stackoverflow.com/questions/7368789/convert-all-strings-in-a-list-to-int
			low,high,sub_sum,total_time = bruteforce2(A,n)
			avg_time += total_time
		avg_time=avg_time/3	
		time1.append(avg_time)
		print("Brute Force")
		print( "max subrray = A["+str(low)+".."+str(high)+"]")
		print("Max Sum = "+str(sub_sum))
		n+=500

	n = 500	
	while(n<=10000):
		avg_time = 0
		for i in range(0,3):
			A = []
			A = list(map(int, string_Numbers[:n]))
			start = time.time()
			low,high,sub_sum = findMaxSubArray(A,0,n-1)
			end = time.time()
			total_time = end - start
			avg_time += total_time
		avg_time=avg_time/3	
		time2.append(avg_time)
		print("Divide And Conquer")
		print( "max subrray = A["+str(low)+".."+str(high)+"]")
		print("Max Sum = "+str(sub_sum))
		n+=500

	plot_graph(time1, time2)
	file.close()
	pass


if __name__ == '__main__':
	main()
