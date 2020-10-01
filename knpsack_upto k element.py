def fun(profit, weight, n, max_weight, max_element):
	dp=[[[0 for i in range(max_element+2)] for j in range(max_weight+2)] for k in range(n+2)]
	for i in dp:
		for j in i:
			print(*j)
	for i in range(1,n+1):
		for j in range(1,max_weight+1):
			for k in range(1,max_element+1):
				if(j>=weight[i-1]):
					
					dp[i][j][k]=max(dp[i-1][j][k], 
					dp[i-1][j-weight[i-1]][k-1]+profit[i-1])
				else:
					dp[i][j][k]=dp[i-1][j][k]
	return dp[n][max_weight][max_element]

n = 5
max_weight=10
max_element=3
profit =  [2, 7, 4, 5, 3 ]
weight = [ 2, 5, 2, 3, 4 ]
a=fun(profit, weight ,5, max_weight, max_element)
print(a)
