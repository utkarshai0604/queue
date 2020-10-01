
import heapq 

def merge(a):
	n=len(a)
	q=[]
	m=len(a[0])
	if m==0:
		return []
	for i in range(n):
		heapq.heappush(q,(a[i][0],i))
	arr=[]
	while len(q):
		top=heapq.heappop(q)
		print(top)
		arr.append(top[0])
		if top[2]==(m-1):
			continue
		x,y=top[1],top[2]+1
		heapq.heappush(q,(a[x][y],x,y))
	return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
	t=int(input())
	for _ in range(t):
		n=int(input())
		numbers=[[ 0 for _ in range(n) ] for _ in range(n) ]
		line=input().strip().split()
		for i in range(n):
			for j in range(n):
				numbers[i][j]=int(line[i*n+j])
		merged_list=merge(numbers)
		for i in merged_list:
			print(i,end=' ')
		print()
# } Driver Code Ends
# if __name__ == '__main__': 
# 	for _ in range(int(input())):
# 		n=int(input())
# 		l=list(map(int, input().split()))
# 		k=0
# 		m=[]
# 		for i in range(n):
# 			a=[]
# 			for j in range(n):
# 				a.append(l[k])
# 				k+=1
# 			m.append(a)
		
# 		merge_k_sorted_arrays(m, len(m)) 

# # The code is contributed by Rajat Srivastava 
