for _ in range(int(input())):
	n,k=map(int, input().split())
	a=[0]*n
	a[0]=1
	a[n-1]=1
	for i in range(0, n, k):
		a[i]=1

	for i in range(n-1, -1, -k):
		a[i]=1
	print(*a)

# https://practice.geeksforgeeks.org/problems/construct-binary-palindrome-by-repeated-appending-and-trimming/0