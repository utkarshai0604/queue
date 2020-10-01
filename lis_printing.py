def lis(arr): 
    n = len(arr) 
    print(arr)
    
    
    lis = [1]*n 
    s=[-99]*n
    max1=-999999
    
    for i in range (1 , n): 
        for j in range(0 , i): 
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 : 
                s[i]   =j
                lis[i] = lis[j]+1
        if(max1<lis[i]):
            index=i
            
            max1=lis[i]
    print(index, *s)
    i=index
    
    n1=[arr[index]]
    while(s[i]!=-99):
        print(i)
        print(arr[s[i]])

        n1.append(arr[s[i]])
        i=s[i]
    print(*n1)
    maximum = 0

    for i in range(n): 
        maximum = max(maximum , lis[i]) 

    return maximum 

arr = [10, 22, 9, 33, 21, 50, 41, 60, 5] 
print ("Length of lis is", lis(arr) )
 
