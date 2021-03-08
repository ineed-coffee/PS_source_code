
# Using dp-list
def solution(n, money):

    L=len(money)
    dp = [1]+[0]*n
    for m in money:
        for j in range(m,n+1):
            dp[j]+=dp[j-m]
    return dp[-1]%1000000007

# Using dp-matrix
def solution(n, money):

    L=len(money)
    dp = [[1]+[0]*n for _ in range(L+1)]

    for i in range(1,L+1):
        for j in range(1,n+1):
            dp[i][j]=int(j-money[i-1]>=0)*dp[i][j-money[i-1]]+dp[i-1][j]

    combs=dp[-1][-1]
    combs=combs%1000000007
    return combs
