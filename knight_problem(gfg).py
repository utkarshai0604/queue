import sys

moves = []
def bfs(n,a,b):
	dist = {}
	start = 0,0
	goal = n-1,n-1
	queue = [start]
	dist[start] = 0
	
	while len(queue):
		cur = queue[0]
		queue.pop(0)
		if cur == goal:
			moves.append(dist[cur]) 
			return
		for move in [ (a,b),(b,a),(-a,-b),(-b,-a),(a,-b),(-a,b),(-b,a),(b,-a) ]:
			next_pos = cur[0]+move[0], cur[1]+move[1]    

			if next_pos[0] > goal[0] or next_pos[1] > goal[1] or next_pos[0] < 0 or next_pos[1] < 0 or (next_pos[0] == 0 and next_pos[1] == 0):
				continue

			if next_pos not in dist:
				dist[next_pos] = dist[cur]+1
				queue.append(next_pos)          
	moves.append(-1)
	
	queue.clear()
	dist.clear()
	return



n = int(input().strip())
# your code goes here
for j in range(1,n):
	for k in range(1,n):
		bfs(n,j,k)
		print("hello\n")
	print(*moves)

	moves.clear()