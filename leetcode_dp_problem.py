#  Dynamic Programming Python implementation of Matrix 
# Chain Multiplication. See the Cormen book for details 
# of the following algorithm 
import sys 

# Matrix Ai has dimension p[i-1] x p[i] for i = 1..n 
def MatrixChainOrder(arr): 
	
	# For simplicity of the program, one extra row and one 
	# extra column are allocated in m[][]. 0th row and 0th 
	# column of m[][] are not used 
	n=len(arr)
	# print("in fun")
	dp=[[0 for i in range(n+1)] for j in range(n+1)]
	for i in range(1,n+1):
		dp[i][i]=arr[i-1]
	
	for L in range(1, n): 
		for i in range(1, n-L+1): 
			
			j = i+L
			# print(i,j)
			for k in range(i, j): 
				dp[i][j] = max(dp[i][k], dp[k + 1][j])
	subArray=dp
	# print(subArray)
	m = [[0 for x in range(n+1)] for x in range(n+1)] 
	# m[i,j] = Minimum number of scalar multiplications needed 
	# to compute the matrix A[i]A[i+1]...A[j] = A[i..j] where 
	# dimension of A[i] is p[i-1] x p[i] 

	# cost is zero when multiplying one matrix. 
	
	# formaxEle=[[0 for i in range(n+1)] for i in range(n+1)]
	# L is chain length. 
	for L in range(1, n): 
		for i in range(1, n-L+1): 
			
			j = L+i
			# print(i,j)
			
			mini=float('inf')
			for k in range(i, j): 

				# q = cost/scalar multiplications 
				q = m[i][k] + m[k + 1][j] + subArray[i][k] * subArray[k + 1][j]
				# print(subArray[i][j], q, "subArray", "cost")
				if q < mini: 
					mini=q
					m[i][j]=mini
	return m[1][n] 




	
				# q = cost/scalar multiplications 
				
				
# Driver program to test above function 
arr = [6, 2, 4] 
size = len(arr) 

print((MatrixChainOrder(arr))) 




# This Code is contributed by Bhavya Jain 
