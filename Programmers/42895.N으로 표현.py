def solution(N, number):
    L=len(str(number))
    max_use=8
    dp= [set() for _ in range(max_use+1)]
    
    def math_permute(set1,set2):
        ret=set()
        for num1 in set1:
            for num2 in set2:
                ret.update([num1+num2,num1-num2,num1*num2])
                if num2:
                    ret.add(num1//num2)
        return ret
    
    for i in range(1,max_use+1):
        dp[i].add(int(str(N)*i))
        for j in range(1,i):
            made=math_permute(dp[j],dp[i-j])
            dp[i]= dp[i]|made
        if number in dp[i]:
            return i
    return -1
