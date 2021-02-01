from sys import *

class queue():
    def __init__(self):
        self.q=[]
        self.L=0
        self.R=0

    def push(self,data):
        self.q.append(data)
        self.R+=1
        return

    def pop(self):
        if self.L==self.R:
            print(-1)
            return
        else:
            print(self.q[self.L])
            self.L+=1
            return
        
    def size(self):
        print(self.R-self.L)
        return
    
    def empty(self):
        if self.L==self.R:
            print(1)
        else:
            print(0)
        return
    
    def front(self):
        if self.L!=self.R:
            print(self.q[self.L])
            return
        print(-1)

    def back(self):
        if self.L!=self.R:
            print(self.q[self.R-1])
            return
        print(-1)


N=int(input())
Q=queue()
commands=[stdin.readline().strip().split() for _ in range(N)]
             

for command in commands:
    if command[0]=='push':
        Q.push(command[1])
    elif command[0]=='pop':
        Q.pop()
    elif command[0]=='size':
        Q.size()
    elif command[0]=='empty':
        Q.empty()
    elif command[0]=='front':
        Q.front()
    else:
        Q.back()
