from sys import *

class Stack():
    def __init__(self):
        self.box=[]

    def solve(self,ps):
        if len(ps)%2==0 and ps[-1]!='(':
            self.box=[]
            for i in ps:
                if i == '(':
                    self.push()
                else:
                    if self.top():
                        self.pop()
                    else :
                        print('NO')
                        return
            if len(self.box)>0:
                print('NO')
            else:
                print('YES')
            return
        else:
            print('NO')
            return

    def push(self):
        self.box.append(1)
        return

    def pop(self):
        del self.box[-1]
        return

    def top(self):
        if len(self.box) > 0 :
            return True
        else:
            return False

stack=Stack()

N=int(input())
PS_input=[list(str(stdin.readline().strip())) for _ in range(N)]

for ps in PS_input:
    stack.solve(ps)

