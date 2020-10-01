# Your task is to complete this function
# Function should return True/False or 1/0
# Graph(graph) is a defaultict of type List
# n is no of Vertices
from collections import defaultdict
def Cycle1(v, visited, g, d):
	visited[v]=1
	d[v]+=1
	for i in g[v]:
		
		if(visited[i]==0):
			
			if(Cycle1(i, visited, g, d)):
				return True
		else:
			if(d[i]>0):
				return True
	d[v]-=1
	return False



def isCyclic(n, g)	:
	visited=[0]*n
	d=defaultdict(int)
	for i in range(n):
		if(Cycle1(i , visited, g, d))==True:
			return True

	# d=defaultdict(int)
	# for i in range(n):
	# 	if(Cycle1(i, visited, g, d))==True:
	# 		return Truen ,graph



#{ 
#  Driver Code Starts

from collections import defaultdict

def creategraph(n, arr, graph):
    i = 0
    while i < 2 * e:
        graph[arr[i]].append(arr[i + 1])
        # graph[arr[i + 1]].append(arr[i])
        i += 2

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n,e = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, arr, graph)
        if isCyclic(n, graph):
            print(1)
        else:
            print(0)
# } Driver Code Ends