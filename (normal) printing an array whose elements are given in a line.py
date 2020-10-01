

# Driver prorgram 
for _ in range(int(input())):
	n=int(input())
	l=list(map(int, input().split()))
	k=n
	while(k>0):
		for i in range(n*n-k, n-k-1, -n):
			print(l[i], end=" ")
		k-=1
	print("")




	

# This code is contributed by 
# Smitha Dinesh Semwal	 
