#!/usr/bin/env python3
#Assignment 2
#Rushabh Ashok Dharia 

def bruteforce(A,n):
	highestsum = 0	#stores the highest sum
	sum_arr = 0	#stores the sum of current sub array
	sub_arr = []
	temp_arr = []
	for i in range(1,n+1):
		counter = 0		
		for j in range(n):
			for k in range(counter,counter+i):
				if(k<n):
					sum_arr += A[k]
					temp_arr.append(A[k])				
			#print(temp_arr)		
			if(highestsum<sum_arr):
				sub_arr = temp_arr
				highestsum = sum_arr
			temp_arr = []
			sum_arr = 0
			counter+=1
			if((counter+i)>n):
				break
	return sub_arr		


def main():
	A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
	n=len(A)
	print(n)
	sub_arr = bruteforce(A,n)
	print("the sub arr is:")
	print(sub_arr)
	pass

if __name__ == '__main__':
	main()
