class Solution:
    def numFactoredBinaryTrees(self, arr) -> int:
        
        L=len(arr)
        dp=[1]*len(arr)
        arr.sort()
        num2idx={v:i for i,v in enumerate(arr)}
        
        for i in range(L):
            for j in range(i):
                if not arr[i]%arr[j] and num2idx.get(arr[i]//arr[j],-1)!=-1:
                    dp[i]+=dp[j]*dp[num2idx[arr[i]//arr[j]]]
        
        answer=sum(dp)
        answer=answer%(10**9 + 7)

        return answer
        
