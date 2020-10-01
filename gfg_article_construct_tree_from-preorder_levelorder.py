from collections import defaultdict

class Node():
	def __init__(self, data):
		self.data=data
		self.left=None
		self.right=None
	

def buildTree(ino, pre, inStr, inEnd, mp):
	print(inStr, inEnd)
	
	if(inStr>inEnd):
		return None
	curr=pre[buildTree.preIndex]
	buildTree.preIndex+=1 # this is how we use preIndex
    #see this carefully

	tNode=Node(curr)
	if(inStr==inEnd):
		print(inStr, inEnd)
		return tNode
	inIndex=mp[curr]
	tNode.left=buildTree(ino, pre, inStr, inIndex-1, mp)
	tNode.right=buildTree(ino, pre, inIndex+1, inEnd, mp)
	
	return tNode


def buildTreeWrap(ino, pre, length):
	d={}
	for i in range(length):
		d[ino[i]]=i
	return buildTree(ino, pre, 0, length-1, d)


def printInorder(root):
	if(not root):
		return
	printInorder(root.left)
	print(root.data)
	printInorder(root.right)


#driver program
inOrder=[ "D", "B", "E", "A", "F", "C" ]
preOrder=["A", "B", "D", "E", "C", "F" ]
buildTree.preIndex=0
root=buildTreeWrap(inOrder, preOrder, len(preOrder))
printInorder(root)