for _ in range(int(input())):
	n=int(input())
	a=list(map(int, input().split()))
	s=list()
	ans=[0]*n
	for i in range(n-1, -1, -1):
		
		while( len(s)>0 and s[-1]<=a[i]):
			s.pop()
		if(len(s)==0):
			ans[i]=0
		else:
			ans[i]=s[-1]
		s.append(a[i])
	print(sum(ans))
		

# https://practice.geeksforgeeks.org/problems/save-gotham/0