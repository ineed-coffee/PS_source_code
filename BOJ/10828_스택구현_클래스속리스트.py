from sys import *

class Stack():
    def __init__(self):
        self.box=[]

    def push(self,num):
        self.box.append(num)

    def top(self):
        if len(self.box) > 0 :
            print(self.box[-1])
        else:
            print(-1)
        return

    def size(self):
        print(len(self.box))
        return

    def empty(self):
        print(0 if len(self.box)>0 else 1)
        return

    def pop(self):
        if len(self.box) > 0 :
            print(self.box[-1])
            del self.box[-1]
        else:
            print(-1)
        return
    

stack=Stack()

N=int(input())
command=[]
for _ in range(N):
    command.append(stdin.readline().strip().split())

for com in command:
    if com[0]=='push':
        stack.push(com[1])
    elif com[0]=='top':
        stack.top()
    elif com[0]=='size':
        stack.size()
    elif com[0]=='empty':
        stack.empty()
    else :
        stack.pop()    
