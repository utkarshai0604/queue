from collections import defaultdict
for _ in range(int(input())):
	n, k=map(int,(input().split()))
	l=list(map(int,(input().split())))
	d=defaultdict(int)
	maxl=0
	for i in l:
		s+=i

		if(s==k):
			maxl=i+1
		elif(s-k in d):
			maxl=max(maxl, i-d[s-k])
		if s not in d:
			d[s]=i
	print(maxl)

