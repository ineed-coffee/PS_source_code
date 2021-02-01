from sys import *
#from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(300000)

class Node():

    def __init__(self,num):
        self.data=num
        self.child_l=None
        self.child_r=None
        self.parent=None

class my_tree():

    def __init__(self):
        self.head=None

    def add(self,node):
        if not self.head:
            self.head=node
            
        else:
            tmp=self.head
            while True:
                if node.data==tmp.data:
                    return
                elif node.data<tmp.data and tmp.child_l:
                    tmp=tmp.child_l
                elif node.data>tmp.data and tmp.child_r:
                    tmp=tmp.child_r
                elif node.data<tmp.data and not tmp.child_l:
                    node.parent=tmp
                    tmp.child_l=node
                    return
                elif node.data>tmp.data and not tmp.child_r:
                    node.parent=tmp
                    tmp.child_r=node
                    return

    def find(self,num):
        tmp=self.head
        while tmp:
            if num==tmp.data:
                print(1)
                return
            elif num<tmp.data:
                tmp=tmp.child_l
            elif num>tmp.data:
                tmp=tmp.child_r
        print(0)
        return


input = stdin.readline
N=int(input())
Arr=[*map(int,input().split())]
Tree= my_tree()
for a in Arr:
    Tree.add(Node(a))
M=int(input())
finds=[*map(int,input().split())]
for f in finds:
    Tree.find(f)




