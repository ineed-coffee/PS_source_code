from sys import *
setrecursionlimit(10000)


def Solve(idx,S,V,Ans):

    if len(Ans)==6:
        print(*Ans)
        return

    for i in range(idx,len(S)):
        if not V[i]:
            V[i]=True
            Ans.append(S[i])
            Solve(i,S,V,Ans)
            Ans.pop()
            V[i]=False
    


while True:

    case = list(map(int,stdin.readline().split()))
    if case[0] ==0:
        break
    k = case[0]
    S = case[1:]
    V=[False]*k
    Ans=[]
    Solve(0,S,V,Ans)
    print()
