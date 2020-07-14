from sys import *

input = stdin.readline

def Trip(room_n):
    global flag,Cash

    if flag:
        return

    for nxt in Room[room_n][2]:
        if Visited[nxt]:
            continue
        
        if Room[nxt][0]=='E':
            if nxt == N:
                flag=True
                return
            else:
                Visited[nxt]=True
                Trip(nxt)
                Visited[nxt]=False
                
        elif Room[nxt][0]=='T':
            if Cash >= Room[nxt][1]:
                if nxt == N:
                    flag=True
                    return
                else:
                    Cash-= Room[nxt][1]
                    Visited[nxt]=True
                    Trip(nxt)
                    Visited[nxt]=False
                    
                    Cash+= Room[nxt][1]

        elif Room[nxt][0]=='L':
            if nxt == N:
                flag=True
                return
            else:
                if Cash < Room[nxt][1]:
                    tmp = Cash
                    Cash = Room[nxt][1]
                    Visited[nxt]=True
                    Trip(nxt)
                    Visited[nxt]=False
                    Cahs = tmp
                else:
                    Visited[nxt]=True
                    Trip(nxt)
                    Visited[nxt]=False
    
while True:
    N = int(input())

    if not N: break

    Cash=0
    Room=[0]
    for n in range(N):
        info = input().split()
        Type = info[0]
        Amount = int(info[1])
        Ports = [*map(int,info[2:-1])]
        Room.append([Type,Amount,Ports])

    flag = False
    Visited=[False]*(N+1)
    Visited[1]=True
    Trip(1)

    if flag:
        print('Yes')
    else:
        print('No')
