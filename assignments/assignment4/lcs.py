#!/usr/bin/env python3
import sys
output = []

#----------------------------------------------------------------------------------------
# Reference Algorithm on page 394 and 395 CLRS. Section 15.4
def printlcs(b,x,i,j):
	if (i == 0 or j == 0):
		return
	if (b[i-1][j-1] == 'cross'):
		printlcs(b,x,i-1,j-1)
		#print(x[i-1])
		output.append(x[i-1])
	elif(b[i-1][j-1]=='up'):
		printlcs(b,x,i-1,j)
	else:
		printlcs(b,x,i,j-1)

def lcs(x,y):
	m = len(x)
	n = len(y)
	b = [[0]*(n) for _ in range(m)]
	c = [[0]*(n+1) for _ in range(m+1)]

	# Don't need this as I am already initializing all the elements of the 2 lists to 0
	# for i in range(1,m):
	# 	c[i][0] = 0
	# for j in range(0,n):
	# 	c[0][j] = 0
	
	for i in range(0,m):
		for j in range(0,n):
			if (x[i] == y[j]):
				c[i+1][j+1] = c[i][j] + 1
				b[i][j] = "cross"
			elif (c[i][j+1]>=c[i+1][j]):
				c[i+1][j+1] = c[i][j+1]
				b[i][j] = "up"
			else :
				c[i+1][j+1] = c[i+1][j]
				b[i][j] = "right"
	return b
#----------------------------------------------------------------------------------------	
#Test Input
# x = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
# y = ['B', 'D', 'C', 'A', 'B', 'A']

# b = lcs(x,y)
# i, j = len(x), len(y)
# printlcs(b,x,i,j)

# print()
# x = [1, 0, 0, 1, 0, 1, 0, 1] 
# y = [0, 1, 0, 1, 1, 0, 1, 1, 0]

# b = lcs(x,y)
# i, j = len(x), len(y)
# printlcs(b,y,i,j)
#----------------------------------------------------------------------------------------
def main():
	X = input("X = ")
	Y = input("Y = ")
	n = len(X)
	m = len(Y)
	x = X[1:(n-1)] # removes '<'' and '>' from input 
	y = Y[1:(m-1)] # removes '<'' and '>' from input
	x = x.split(",") # converts string to list
	y = y.split(",") # converts string to list

	b = lcs(x,y) #generates 2d arrays b and c. Only require b to print the LCS
	i, j = len(x), len(y)
	printlcs(b,x,i,j) #Stores the output in the list 'output'

	#Printing the output
	print("Output = ", end = "")
	print("<",end="")
	for i in range(len(output)):		
		if(i<(len(output)-1)):
			print(output[i],end=',')
		else:
			print(output[i], end='>')
	print()
	pass

if __name__ == '__main__':
	main()
