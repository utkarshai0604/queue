class node1():
    def __init__(self, val):
        self.val=val
        self.right=None
        self.left=None

    def levelOrder(self, root):
        q1=[]
        q2=[]
        q1.append(root)
        
        while(len(q1)>0 or len(q2)>0):
            s1=""
            
            while(len(q1)>0):
                node=q1.pop(0)
                
                s1+=node.val+" "
                if(node.left):
                    q2.append(node.left)
                    
                if(node.right):
                    q2.append(node.right)
                    
            print(s1)
            s1=""

            s2=""
            while(len(q2)>0):
                node=q2.pop(0)
                
                s2+=node.val+" "
                if(node.left):
                    q1.append(node.left)
                if(node.right):
                    q1.append(node.right)
            print(s2)
            s2=""



node = node1("1") 
node.left = node1("2") 
node.right = node1("3") 
node.left.left = node1("4") 
node.left.right = node1("5") 
node.right.right = node1("6") 
node.levelOrder(node)
            

# similar method for spiral traversal onluy change is that we have to use stack.