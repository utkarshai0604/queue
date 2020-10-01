import sys
max=sys.maxsize
mini=-1*max-1
# print(max, mini)
class Node: 
      
    # Constructor to create a new node 
    def __init__(self, data): 
        self.key = data 
        self.left = None
        self.right = None

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


def isBSTUtil(node, mini, maxi): 
      
    # An empty tree is BST 
    if node is None: 
        return True
  
    # False if this node violates min/max constraint 
    if node.key < mini or node.key > maxi: 
        return False
  
    # Otherwise check the subtrees recursively 
    # tightening the min or max constraint 
    return (isBSTUtil(node.left, mini, node.key -1) and
          isBSTUtil(node.right, node.key+1, maxi)) 

def isBST(root):
    
    return (isBSTUtil(root, -9999999999, 9999999999))

print(max, mini)
max=float('inf')
mini=(float('-inf'))
k=99999


root = Node(8) 

root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 
print(isBST(root ))