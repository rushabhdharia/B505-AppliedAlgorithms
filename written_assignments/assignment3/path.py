def path(n,m):
	if(A[n][m]>-1):
		return A[n][m]
	elif((n==1 and m == 0) or (n==0 and m ==1)):
		return 1
	elif(n==0):
		A[n][m] = path(n,m-1)
	elif(m==0):
		A[n][m] = path(n-1,m)
	else:
		A[n][m] = path(n,m-1)+path(n-1,m)

	return A[n][m]

n = 4
m = 3
A = [[-1 for j in range(m+1)] for i in range(n+1)]
print(path(n,m))
