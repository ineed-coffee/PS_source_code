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


input=stdin.readline

N=int(input())
dq=Make_deque()
for n in range(N):
    command=input().strip().split()
    if command[0]=='push_back':
        dq.pub(Node(int(command[1])))
    elif command[0]=='push_front':
        dq.puf(Node(int(command[1])))
    elif command[0]=='front':
        dq.front()
    elif command[0]=='back':
        dq.back()
    elif command[0]=='size':
        dq.size()
    elif command[0]=='empty':
        dq.empty()
    elif command[0]=='pop_front':
        dq.pof()
    elif command[0]=='pop_back':
        dq.pob()
