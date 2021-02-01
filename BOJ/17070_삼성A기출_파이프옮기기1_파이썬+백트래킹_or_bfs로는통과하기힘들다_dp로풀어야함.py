from sys import *
from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(10000)

    
def back_track(tail,head):
    global Ans
    
    if head == [N-1,N-1]:
        Ans+=1
        return

    if tail[0]==head[0]:
        c_hx,c_hy = head

        for d in [[0,1],[1,1]]:
            n_hx,n_hy = c_hx+d[0],c_hy+d[1]
            if (0<=n_hx<N)and(0<=n_hy<N):
                if d==[0,1] and not House[n_hx][n_hy]:
                    back_track([c_hx,c_hy],[n_hx,n_hy])
                elif d==[1,1] and not House[n_hx][n_hy] and not House[n_hx-1][n_hy] and not House[n_hx][n_hy-1]:
                    back_track([c_hx,c_hy],[n_hx,n_hy])
                
    elif head[0]==tail[0]+1:
        
        if head[1]==tail[1]:
            c_hx,c_hy = head

            for d in [[1,0],[1,1]]:
                n_hx,n_hy = c_hx+d[0],c_hy+d[1]
                if (0<=n_hx<N)and(0<=n_hy<N):
                    if d==[1,0] and not House[n_hx][n_hy]:
                        back_track([c_hx,c_hy],[n_hx,n_hy])
                    elif d==[1,1] and not House[n_hx][n_hy] and not House[n_hx-1][n_hy] and not House[n_hx][n_hy-1]:
                        back_track([c_hx,c_hy],[n_hx,n_hy])

            
        else:
            c_hx,c_hy = head

            for d in [[0,1],[1,0],[1,1]]:
                n_hx,n_hy = c_hx+d[0],c_hy+d[1]
                if (0<=n_hx<N)and(0<=n_hy<N):
                    if d==[1,0] and not House[n_hx][n_hy]:
                        back_track([c_hx,c_hy],[n_hx,n_hy])
                    elif d==[0,1] and not House[n_hx][n_hy]:
                        back_track([c_hx,c_hy],[n_hx,n_hy])
                    elif d==[1,1] and not House[n_hx][n_hy] and not House[n_hx-1][n_hy] and not House[n_hx][n_hy-1]:
                        back_track([c_hx,c_hy],[n_hx,n_hy])


def bfs(tail,head):
    global Ans

    que = deque([[tail,head]])

    while que:

        c_tail,c_head = que.popleft()
        c_tx,c_ty=c_tail
        c_hx,c_hy=c_head

        if c_hx==N-1 and c_hy==N-1:
            Ans+=1
            continue

        if c_tx==c_hx:

            for d in [[0,1],[1,1]]:
                n_hx,n_hy = c_hx+d[0],c_hy+d[1]
                if (0<=n_hx<N)and(0<=n_hy<N):
                    if d==[0,1] and not House[n_hx][n_hy]:
                        que.append([[c_hx,c_hy],[n_hx,n_hy]])
                    elif d==[1,1] and not House[n_hx][n_hy] and not House[n_hx-1][n_hy] and not House[n_hx][n_hy-1]:
                        que.append([[c_hx,c_hy],[n_hx,n_hy]])
                
        elif c_hx==c_tx+1:
        
            if c_hy==c_ty:

                for d in [[1,0],[1,1]]:
                    n_hx,n_hy = c_hx+d[0],c_hy+d[1]
                    if (0<=n_hx<N)and(0<=n_hy<N):
                        if d==[1,0] and not House[n_hx][n_hy]:
                            que.append([[c_hx,c_hy],[n_hx,n_hy]])
                        elif d==[1,1] and not House[n_hx][n_hy] and not House[n_hx-1][n_hy] and not House[n_hx][n_hy-1]:
                            que.append([[c_hx,c_hy],[n_hx,n_hy]])

            
            else:

                for d in [[0,1],[1,0],[1,1]]:
                    n_hx,n_hy = c_hx+d[0],c_hy+d[1]
                    if (0<=n_hx<N)and(0<=n_hy<N):
                        if d==[1,0] and not House[n_hx][n_hy]:
                            que.append([[c_hx,c_hy],[n_hx,n_hy]])
                        elif d==[0,1] and not House[n_hx][n_hy]:
                            que.append([[c_hx,c_hy],[n_hx,n_hy]])
                        elif d==[1,1] and not House[n_hx][n_hy] and not House[n_hx-1][n_hy] and not House[n_hx][n_hy-1]:
                            que.append([[c_hx,c_hy],[n_hx,n_hy]])
    
#--------------------------------------------------------------

input = stdin.readline

N = int(input())

House = [list(map(int,input().split())) for _ in range(N)]
Ans =0

bfs([0,0],[0,1])
print(Ans)
