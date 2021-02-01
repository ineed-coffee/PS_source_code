from sys import *
#from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(100000)

class Node():
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.nxt=None


class Make_deque():

    def __init__(self):
        self.head=None
        self.tail=None
        self.r=False

    def push(self,node):
        if self.head:
            self.tail.nxt=node
            node.prev=self.tail
            self.tail=node
        else:
            self.head=node
            self.tail=node

    def pob(self):
        global flag
        if not self.tail:
            flag=True
            return
        
        self.tail=self.tail.prev
        if not self.tail:
            self.head=None
        else:
            self.tail.nxt=None

    def pof(self):
        global flag
        if not self.head:
            flag=True
            return

        self.head=self.head.nxt
        if not self.head:
            self.tail=None
        else:
            self.head.prev=None

    def reverse(self):
        if self.r:self.r=False
        else:self.r=True

    def delete(self):
        if self.r:
            self.pob()
        else:
            self.pof()

    def out(self):
        return_list=[]
        if self.r:
            start=self.tail
            while True:
                if not start:
                    return ','.join(return_list)
                else:
                    return_list.append(str(start.data))
                    start=start.prev
        else:
            start=self.head
            while True:
                if not start:
                    return ','.join(return_list)
                else:
                    return_list.append(str(start.data))
                    start=start.nxt

input=stdin.readline

T = int(input())
for test in range(T):
    Commands=input().strip()
    N=int(input())
    Arr = input().strip().split(',')
    Dq=Make_deque()
    for a in range(N):
        if not a :
            if N==1:
                Dq.push(Node(int(Arr[a][1:-1])))
            else:
                Dq.push(Node(int(Arr[a][1:])))
        elif a==N-1:
            Dq.push(Node(int(Arr[a][:-1])))
        else:
            Dq.push(Node(int(Arr[a])))

    Commands = Commands.split('D')
    flag=False
    for c in range(len(Commands)):
        if flag:
            break
        if len(Commands[c])%2:
            Dq.reverse()
        if c!=len(Commands)-1:
            Dq.delete()
    if flag:
        print('error')
    else:
        print('['+Dq.out()+']')
    
'''
class Node():
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.nxt=None


class Make_deque():

    def __init__(self):
        self.head=None
        self.tail=None
        self.len=0

    def pub(self,node):
        self.len+=1
        if self.tail:
            self.tail.nxt=node
            node.prev=self.tail
            self.tail=node
        else:
            self.head=node
            self.tail=node

    def puf(self,node):
        self.len+=1
        if self.head:
            self.head.prev=node
            node.nxt=self.head
            self.head = node
            
        else:
            self.head=node
            self.tail=node

    def pob(self):
        
        if not self.tail:
            print(-1)
            return
        self.len-=1
        print(self.tail.data)
        self.tail=self.tail.prev
        if not self.tail:
            self.head=None
        else:
            self.tail.nxt=None

    def pof(self):
        
        if not self.head:
            print(-1)
            return
        self.len-=1
        print(self.head.data)
        self.head=self.head.nxt
        if not self.head:
            self.tail=None
        else:
            self.head.prev=None

    def size(self):
        print(self.len)

    def empty(self):
        print(1 if not self.head else 0)

    def front(self):
        if not self.head:
            print(-1)
        else:
            print(self.head.data)

    def back(self):
        if not self.tail:
            print(-1)
        else:
            print(self.tail.data)
'''
