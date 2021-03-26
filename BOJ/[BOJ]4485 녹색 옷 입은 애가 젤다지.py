import sys

input = sys.stdin.readline

if __name__ == "__main__":
    from collections import deque
    from heapq import heappush,heappop

    idx=1
    while True:
        N = int(input().strip())
        if not N:break

        board= [[*map(int,input().split())] for _ in range(N)]

        dist={}
        for i in range(N):
            for j in range(N):
                if (not i) and (not j):
                    dist[(i,j)]=board[i][j]
                else:
                    dist[(i,j)]=float("inf")
        
        dx = [0,1,0,-1]
        dy = [-1,0,1,0]
        que=[]
        heappush(que,[board[0][0],(0,0)])

        while que:
            csum,(cx,cy)=heappop(que)

            if csum>dist[(cx,cy)]:
                continue

            for i in range(4):
                nx,ny=cx+dx[i],cy+dy[i]
                if (0<=nx<N) and (0<=ny<N):
                    if csum+board[nx][ny]<dist[(nx,ny)]:
                        dist[(nx,ny)]=csum+board[nx][ny]
                        heappush(que,[csum+board[nx][ny],(nx,ny)])

        print("Problem "+str(idx)+":",dist[(N-1,N-1)])
        idx+=1
