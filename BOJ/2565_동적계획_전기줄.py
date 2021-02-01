from sys import*

def LIS_solve(array,length):

    dp=[1]*length
    for i in range(1,length):
        for j in range(i):
            if array[i][1]>array[j][1]:
                dp[i]=max(dp[j]+1,dp[i])
    return length-max(dp)

def Rearrange(list_ex):
    if len(list_ex)<=1:
        return list_ex
    else:
        pivot=list_ex[0][0]
        low,high=[],[]
        for i in range(1,len(list_ex)):
            if list_ex[i][0]<pivot:
                low.append(list_ex[i])
            else:
                high.append(list_ex[i])
    return Rearrange(low)+[list_ex[0]]+Rearrange(high)

line_num=int(input())
line_match=[]
for _ in range(line_num):
    line_match.append(list(map(int,stdin.readline().strip().split())))
    
line_match = Rearrange(line_match)
print(LIS_solve(line_match,line_num))
