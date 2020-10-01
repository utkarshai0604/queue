# Python program to find LCA of n1 and n2 using one 
# traversal of Binary tree 

# A binary tree node 
class Node: 
	
	# Constructor to create a new tree node 
	def __init__(self, key): 
		self.key = key 
		self.left = None
		self.right = None
	
# This function returns pointer to LCA of two given 
# values n1 and n2 
# This function assumes that n1 and n2 are present in 
# Binary Tree 
# method 1 subpart
def balanceChk(root):
    if(root==None):
        return 0
    lh=balanceChk(root.left)
    if(lh==-1):
        return -1
    
    rh=balanceChk(root.right)
    if(rh==-1):
        return -1

    if(abs(lh-rh)>1):
        return -1
    else:
        return 1+max(lh, rh)
    

# method 1 
def balance(root):
    if(balanceChk(root)==-1):
        return False
    return True


# method 2
def check_balanced(root): 
    if root is None:
        return 0
    l = check_balanced(root.left)
    r = check_balanced(root.right)
    if l is False or r is False:
        return False
    if abs(l-r)>1:
        return False
    else:
        return max(l,r)+1

	
# Driver program to test above function 

# Let us create a binary tree given in the above example 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 


print(balance(root))

if(check_balanced(root)):
    print("True")
else:
    print("False")
# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
