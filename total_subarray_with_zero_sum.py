from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int, input().split()))

    d=defaultdict(list)
    s=0
    a=[]
    b=[]
    c=0
    for i in range(len(arr)):
        s+=arr[i ]
       
        if(s==0):
            c+=1
            a.append(0)
            b.append(i)
        if s in d:
       
            abc=d[s]
            for j in abc:
                c+=1
                a.append(j+1)
                b.append(i)
        d[s].append(i)
    print(c)