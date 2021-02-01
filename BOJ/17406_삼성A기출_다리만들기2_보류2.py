from sys import *
from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(10000)

def bfs(x,y):
    global Visited

    Visited[x][y]=True
    que = deque([[x,y]])
    group=[[x,y]]
    while que:
        cx,cy=que.popleft()

        for d in [[0,1],[1,0],[0,-1],[-1,0]]:
            nx,ny=cx+d[0],cy+d[1]
            if (0<=nx<10) and (0<=ny<10) and not Visited[nx][ny] and Board[nx][ny]:
                Visited[nx][ny]=True
                que.append([nx,ny])
                group.append([nx,ny])
    return group


def back_track(num):
#    print(num)
    global Quan,cnt,Ans
    
    if not num:
        Ans = min(cnt,Ans) if Ans else cnt
        return

    if Ans and cnt>Ans:
        return
    
    for cord in Group:
        x,y = cord
        if not Board[x][y]:
            continue
        for size in range(5,0,-1):
            
            if Size_match(x,y,size):
                if Quan[size]:
                    fill(x,y,size,1)
                    Quan[size]-=1
                    cnt+=1
                    back_track(num-(size**2))
                    cnt-=1
                    Quan[size]+=1
                    fill(x,y,size,0)
                            
                else:
                    return
    return


def Size_match(i,j,s):

    for r in range(s):
        for c in range(s):
            if not((0<=i+r<10) and (0<=j+c<10)) or not Board[i+r][j+c]:
                return False
    return True


def fill(i,j,s,mode):
    global Board

    f = 1 -mode
    for r in range(s):
        for c in range(s):
            Board[i+r][j+c]=f
    return 

#--------------------------------------------------------------

input = stdin.readline
Board = [list(map(int,input().split())) for _ in range(10)]
Group=[]
Ans =0
Quan={1:5,2:5,3:5,4:5,5:5}
Visited=[[False]*10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        if not Visited[i][j] and Board[i][j]:
#            Group.append(bfs(i,j))
            Group+=bfs(i,j)


ones = len(Group)
if ones:
    cnt=0
    back_track(ones)
    if not cnt:
        Ans = -1

print(Ans)


'''
G = len(Group)
for g in range(G):
    cnt=26
    comp=0
    ones = len(Group[g])
    back_track(g,ones)
    if cnt==26:
        Ans = -1
        break
    else:
        Ans+=cnt
'''    

