from sys import *
from collections import deque
#setrecursionlimit(100000)

def fall():
    global Field
    for j in range(6):
        shift=[]
        for i in range(12):
            if Field[i][j]!='.':
                shift.append(Field[i][j])
                Field[i][j]='.'
        for k in range(12-len(shift),12):
            Field[k][j]=shift[k-(12-len(shift))]
                    
    return


def bfs_s(x,y,group):
    global Visited
    
    Letter = Field[x][y]
    Visited[x][y] = True
    que = deque([[x,y]])
    group.append([x,y])
    while que:
        c_x,c_y=que.popleft()
        for i in range(4):
            nx = c_x + dx[i]
            ny = c_y + dy[i]
            if (0<=nx<12)and(0<=ny<6):
                if not Visited[nx][ny] and Field[nx][ny]==Letter:
                    Visited[nx][ny]=True
                    que.append([nx,ny])
                    group.append([nx,ny])                
    return group if len(group)>=4 else []
                    
                

    

dx=[-1,0,1,0]
dy=[0,-1,0,1]
Field = [list(stdin.readline().strip()) for _ in range(12)]
total_pop=0
while True:
    Visited=[[False]*6 for _ in range(12)]
    this_pop=[]
    for i in range(12):
        for j in range(6):
            if not Visited[i][j] and Field[i][j]!='.':
                temp = bfs_s(i,j,[])
                this_pop+=temp
    if not this_pop:
        break
    
    total_pop+=1
    for coord in this_pop:
        Field[coord[0]][coord[1]]='.'
        
    fall()

print(total_pop)
