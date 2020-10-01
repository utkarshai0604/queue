# Your task is to complete this function
# Function should return Topologically Sorted List
# Graph(adj) is a defaultict of type List
# n is no of edges

def top1(v, visited, g, a):
	visited[v]=True
	for i in g[v]:
		if(visited[i]==False):
			top1(i, visited, g, a)
	a.append(v)
	


def topoSort(n, g):
	a=[]
	visited=[False]*n
	for i in range(n):
		if(visited[i]==False):
			top1(i , visited, g, a)
	a.reverse()
	return a





#{ 
#  Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
def creategraph(e, n, arr, graph):
    i = 0
    while i<2*e:
        graph[arr[i]].append(arr[i+1])
        i+=2
        
def check(graph, N, res):
	map=[0]*N
	for i in range(N):
		map[res[i]]=i
	for i in range(N):
		for v in graph[i]:
			if map[i] > map[v]:
				return False
	return True

from collections import defaultdict
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, N, arr, graph)
        res = topoSort(N, graph)
        
        if check(graph, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends