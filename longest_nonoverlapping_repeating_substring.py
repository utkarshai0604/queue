for _ in range(int(input())):
    n=int(input())
    s=input()
    
    dp=[[0]*(n+1)]*(n+1)
    maxy=-9999999999
    index=0
    for i in range(1, n+1)    :
        for j in range(1, n+1) :
            if(s[i-1]==s[j-1] and (i-j)>dp[i-1][j-1]):
                # just checking the longest distance between them     have to  be maximum of the substring we have found so far
                dp[i][j]=dp[i-1][j-1]+1
                if(maxy<dp[i][j]):
                    maxy=dp[i][j]
                    index=i

    if(maxy!=-9999999999):
        print(maxy, index)
        l=s[index-maxy:index]
        print(l)
    else:
        print(-1)
