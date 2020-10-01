
# return the number of subarrays with equal 0s and 1s
from collections import defaultdict
def countSubarrWithEqualZeroAndOne(arr, N):
    d=defaultdict(int)
    n=N
    cur_sum=0
    a=0
    for i in range(n):
        if(arr[i]==0):
            arr[i]=-1
    for i in range(n):
        cur_sum+=arr[i]
        d[cur_sum]+=1
    
    for i in d:
        s=d[i]
        if(i==0):
            a+=1
            continue
        n=(s*(s-1))//2
        a+=n
    return a
        
        




def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        
        
        print(countSubarrWithEqualZeroAndOne(arr, n))
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends