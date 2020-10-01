from heapq import heappop, heappush, heapify 
for _ in range(int(input())):
	n=int(input())
	l=list(map(int, input().split()))
	k=int(input())
	l1=[]
	for i in range(k):
		abc=-1*l[i]
		l1.append(abc)
	
	
	heapify(l1)	
	for i in range(k, n):
		a=heappop(l1)
		a=-1*a
		
		if(a>l[i]):
			heappush(l1,-1*l[i])
		else:
			heappush(l1, -1*a)
	print(-1*heappop(l1))
		
	


# li=[4,3,2,5,6]
# heapify(li)
# for i in range(5):
# 	a=heappop(li)
# 	print(a)