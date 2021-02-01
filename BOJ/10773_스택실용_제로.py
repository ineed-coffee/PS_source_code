from sys import *

class Stack():
    def __init__(self):
        self.box=[]

    def command(self,com_type):
        if com_type:
            self.push(com_type)
            return
        else:
            self.pop()
            return

    def push(self,num):
        self.box.append(num)
        return

    def pop(self):
        if len(self.box) > 0 :
            del self.box[-1]
        return
    

stack=Stack()

N=int(input())
commands=[int(stdin.readline().strip()) for _ in range(N)]

for com in commands:
    stack.command(com)
print(sum(stack.box))
