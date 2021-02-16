def solution(money):
    answer=0    
    for start in [1,2]:
        dp=[0]*start+money[start-1:]
        for i in range(len(dp)):
            if i<=2:
                dp[i]=(dp[i],i==1)
            else:
                if dp[i-2][0]<dp[i-3][0]:
                    dp[i]=(dp[i]+dp[i-3][0],dp[i-3][1])
                else:
                    dp[i]=(dp[i]+dp[i-2][0],dp[i-2][1])
        
        dp[-1]=dp[-1] if not dp[-1][1] else (dp[-1][0]-dp[1][0],dp[-1][1])
        answer=max(answer,max(dp)[0])
    return answer
