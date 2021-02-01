N = int(input())
Stairs=[[1]*10 for _ in range(N)]
Stairs[0][0]=0
for i in range(1,N):
    for j in range(10):
        if j==0:
           Stairs[i][j]=Stairs[i-1][j-1]
        elif j==9:
            Stairs[i][j]=Stairs[i-1][j-1]
        else:
            Stairs[i][j]=Stairs[i-1][j+1]+Stairs[i-1][j-1]
            
mod=1000000000
Count=sum(Stairs[-1])
print(Count%mod)
