#Reference Bell Triangle
# en.wikipedia.org/wiki/Bell_triangle

def partition(n):
	bell_triangle = [[0 for i in range(n)] for j in range(n)]

	for i in range(0,n):
		for j in range(0,i+1):
			if((i==0 and j==0) or (i==1 and j==0)):
				bell_triangle[i][j]=1
			elif(j==0):
				bell_triangle[i][j]=bell_triangle[i-1][i-1]

			else:
				bell_triangle[i][j] = bell_triangle[i-1][j-1]+bell_triangle[i][j-1]

	for i in range(n):
		for j in range(i+1):
			print(bell_triangle[i][j], end =" ")
		print()
	print()
	return(bell_triangle[n-1][n-1])

n = 5
print("Number of ways a set of length",n,"can be partitioned =",partition(5))

