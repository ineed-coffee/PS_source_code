import sys

input = sys.stdin.readline



def splash_ratio(c,dir_):
    x,y=c
    if dir_==0:
        ret=[(x-2,y,0.02),
             (x-1,y-1,0.1),
             (x-1,y,0.07),
             (x-1,y+1,0.01),
             (x,y-2,0.05),
             (x+2,y,0.02),
             (x+1,y-1,0.1),
             (x+1,y,0.07),
             (x+1,y+1,0.01)
             ]
    elif dir_==1:
        ret=[(x-1,y-1,0.01),
             (x-1,y+1,0.01),
             (x,y-2,0.02),
             (x,y-1,0.07),
             (x,y+1,0.07),
             (x,y+2,0.02),
             (x+1,y-1,0.1),
             (x+1,y+1,0.1),
             (x+2,y,0.05)
             ]
    elif dir_==2:
        ret=[(x-2,y,0.02),
             (x-1,y-1,0.01),
             (x-1,y,0.07),
             (x-1,y+1,0.1),
             (x,y+2,0.05),
             (x+2,y,0.02),
             (x+1,y+1,0.1),
             (x+1,y,0.07),
             (x+1,y-1,0.01)
             ]
    else:
        ret=[(x-2,y,0.05),
             (x+1,y-1,0.01),
             (x+1,y+1,0.01),
             (x,y-2,0.02),
             (x,y-1,0.07),
             (x,y+1,0.07),
             (x,y+2,0.02),
             (x-1,y-1,0.1),
             (x-1,y+1,0.1)
             ]
    return ret



if __name__ == "__main__":


    N = int(input().strip())


    board = [ [*map(int,input().split())] for _ in range(N)]

    cx,cy=N//2,N//2

    splash=0
    dir_=[(0,-1),(1,0),(0,1),(-1,0)]
    lens=[]
    for i in range(1,N-1):
        lens+=[i]*2
    lens+=[N-1]*3
    i=0

    for len_ in lens:
        for _ in range(len_):
            mx,my = cx+dir_[i][0],cy+dir_[i][1]
            splash_coords=splash_ratio((mx,my),i)
            in_grid=0
            for nx,ny,r in splash_coords:
                amount=int(board[mx][my]*r)
                in_grid+=amount
            
                if (0<=nx<N) and (0<=ny<N):
                    board[nx][ny]+=amount
                else:
                    splash+=amount
                    
            board[mx][my]-=in_grid
            a_x,a_y = mx+dir_[i][0],my+dir_[i][1]
            if (0<=a_x<N) and (0<=a_y<N):
                board[a_x][a_y]+=board[mx][my]
            else:
                splash+=board[mx][my]
            board[mx][my]=0
            cx,cy=mx,my

        i=(i+1)%4
        
    print(splash)
