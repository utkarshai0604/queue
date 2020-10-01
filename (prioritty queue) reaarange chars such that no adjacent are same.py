from queue import PriorityQueue
from collections import defaultdict
# https://practice.geeksforgeeks.org/problems/rearrange-characters/0
def fun(s):
    # s="axiqenxohssbtwwwwwwwwwwwwwww"

    d=defaultdict(int)
    q=PriorityQueue()
    ans=[]
    for i in s:
        d[i]+=1
    for i in d:
        q.put([-1*d[i], i])
    while q.qsize()>1:
        next_item = q.get()
        next_item1 = q.get()
        ans.append(next_item[1])
        ans.append(next_item1[1])
        # print(next_item, next_item1)
        next_item[0]+=1
        next_item1[0]+=1
        
        if(next_item[0]):
            q.put(next_item)
        if(next_item1[0]):
            q.put(next_item1)
    if(q.qsize()):
        # print("hello")
        a=q.get()
        # print(a)
        if(a[0]<-1):
            # print(0)
            return 0
            # print("dpne")
        ans.append(a[1])
    print(ans)  
    return 1
        

        # print(next_item)

for _ in range(int(input())):
    s=input()
    print(fun(s))