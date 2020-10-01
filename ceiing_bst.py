class Node: 
      
    # Constructor to create a new node 
    def __init__(self, data): 
        self.key = data 
        self.left = None
        self.right = None

def floor(root, data):
    if(not root):
        return 999
    if(root.key==data):
	    return root.key
    if(data<root.key):
        return floor(root.left, data)
    val=floor(root.right, data)
    if(data >=val):
        return val
    else:
        return root.key

def ceil(root, data):
	if(not root):
		return -1
	if(root.key==data):
		return root.key
	if(data>root.key):
		return ceil(root.right, data)
	
	val=ceil(root.left, data)
	if(data<=val):
		return val
	else:
		return root.key





root = Node(8) 

root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 
  
for i in range(16): 
    print( "% d % d" %(i, ceil(root, i)) )

for i in range(16): 
    print( "% d % d" %(i, floor(root, i)) )