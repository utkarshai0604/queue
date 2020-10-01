class Node: 
      
    # Constructor to create a new node 
    def __init__(self, data): 
        self.key = data 
        self.left = None
        self.right = None

from collections import defaultdict
def varticalTraversal(root, s, d):
	if(not root):
		return
	d[s].append(root.key)
	varticalTraversal(root.left, s-1, d)
	varticalTraversal(root.right, s+1, d)



def vertical(root):
	d=defaultdict(list)
	store=0
	varticalTraversal(root, store, d)
	abc={k: v for k, v in sorted(d.items(), key=lambda item: item[0])}
	print(abc)
    
	for i in abc:
		print(*abc[i])


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
# root.right.left = Node(6) 
root.right.right = Node(6) 
# root.right.left.right = Node(8) 
# root.right.right.right = Node(9)
vertical(root)