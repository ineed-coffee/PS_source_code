from sys import *
input = stdin.readline

R,C,N = map(int,input().split())
Board=[]
Table = [[0]*C for _ in range(R)]
for i in range(R):
    line = list(input().rstrip())
    for j in range(C):
        if line[j]=='O':
            Table[i][j]+=2
    Board.append(line)

D = [[1,0],[0,1],[-1,0],[0,-1]]
for t in range(1,N+1):
    if t==1:
        continue

    for i in range(R):
        for j in range(C):
            Table[i][j]+=1
            
    if t%2:
        for i in range(R):
            for j in range(C):
                if Table[i][j]==4:
                    Table[i][j]=0
                    for dx,dy in D:
                        nx,ny = i+dx,j+dy
                        if not ((0<=nx<R)and(0<=ny<C)):
                            continue

                        if Table[nx][ny]==4:
                            continue
                        Table[nx][ny]=0  
    
for row in Table:
    for col in row:
        if col:
            print('O',end='')
        else:
            print('.',end='')
    print()


'''
    for row in Table:
        print(row)
    print('------------------------------')
    
'''

