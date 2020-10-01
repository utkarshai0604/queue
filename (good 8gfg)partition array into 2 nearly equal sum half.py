for _ in range(int(input())):
    n=int(input())
    
    l=list(map(int, input().split()))
    su=sum(l)
    dp=[[0]*(su+1) for j in range(n+1)]
    for i in range(n+1):
        dp[i][0]=True
    for i in range(1,su+1):
        dp[0][i]=False
    for i in range(1,n+1):
        for j in range(1, su+1):
            dp[i][j]=dp[i-1][j]
            if (l[i-1]<=j):
                dp[i][j] |= dp[i-1][j-l[i-1]]

    dif=999999999999
    for i in range(su//2, -1, -1):
        if(dp[n][i]==True):
            dif=su-(2*i)
            break
    print(dif)

# https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/
# Partition a set into two subsets such that the difference of subset sums is minimum

