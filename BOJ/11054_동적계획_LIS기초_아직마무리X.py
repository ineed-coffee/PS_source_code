from sys import*

def Solve(array,length):

    dp_low=[1]*length
    dp_high=[1]*length
    dp=[1]*length
    for i in range(1,N):
        for j in range(N):
            if array[i]>array[j]:
                dp_high[i]=max(dp_high[j]+1,dp_high[i])
            elif array[i]<array[j]:
                dp_low[i]=max(dp_low[j]+1,dp_low[i])
        dp[i]=dp_high[i]+dp_low[i]-1
    return dp


N=int(input())

Arr=list(map(int,stdin.readline().strip().split()))

print(Solve(Arr,N))

