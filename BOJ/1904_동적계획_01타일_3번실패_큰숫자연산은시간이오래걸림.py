def Tile_prob(N):
    if N==1:
        return 1 
    elif N==2:
        return 2
    else:
        #Tile=[1,2,3]
        prev2=1
        prev1=2
        for i in range(2,N):
            ans=(prev2+prev1)%15746
            prev2=prev1
            prev1=ans
        return ans
    
N = int(input().strip())
print(Tile_prob(N))

