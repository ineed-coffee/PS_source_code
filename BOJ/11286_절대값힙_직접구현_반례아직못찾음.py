from sys import *
#from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(300000)

class make_heap():
    def __init__(self):
        self.hp=[None]


    def push(self,num):

        if len(self.hp)==1:
            self.hp.append(num)
            return
        
        self.hp.append(num)
        cur_loc = len(self.hp)-1
        while cur_loc>1:
            parent_loc=cur_loc//2
            if abs(self.hp[cur_loc])<abs(self.hp[parent_loc]):
                self.hp[cur_loc],self.hp[parent_loc]=self.hp[parent_loc],self.hp[cur_loc]
                cur_loc=parent_loc
            elif abs(self.hp[cur_loc])==abs(self.hp[parent_loc]) and self.hp[cur_loc]<self.hp[parent_loc]:
                self.hp[cur_loc],self.hp[parent_loc]=self.hp[parent_loc],self.hp[cur_loc]
                cur_loc=parent_loc
            else:
                return

    def root_pop(self):

        if len(self.hp)==1:
            print(0)
            return
        self.hp[1],self.hp[-1]=self.hp[-1],self.hp[1]
        print(self.hp.pop())

        cur_loc=1
        while True:
            cur_child_L=cur_loc*2
            cur_child_R=cur_loc*2+1

            if cur_child_L>=len(self.hp):
                return
            elif cur_child_R>=len(self.hp):
                if abs(self.hp[cur_loc])>abs(self.hp[cur_child_L]):
                    self.hp[cur_loc],self.hp[cur_child_L]=self.hp[cur_child_L],self.hp[cur_loc]
                elif abs(self.hp[cur_loc])==abs(self.hp[cur_child_L]) and self.hp[cur_loc]>self.hp[cur_child_L]:
                    self.hp[cur_loc],self.hp[cur_child_L]=self.hp[cur_child_L],self.hp[cur_loc]
                return
            else:
                if abs(self.hp[cur_child_L])>abs(self.hp[cur_child_R]):
                    if abs(self.hp[cur_loc])>abs(self.hp[cur_child_R]):
                        self.hp[cur_loc],self.hp[cur_child_R]=self.hp[cur_child_R],self.hp[cur_loc]
                        cur_loc=cur_child_R
                    elif abs(self.hp[cur_loc])==abs(self.hp[cur_child_R]) and self.hp[cur_loc]>self.hp[cur_child_R]:
                        self.hp[cur_loc],self.hp[cur_child_R]=self.hp[cur_child_R],self.hp[cur_loc]
                        cur_loc=cur_child_R
                    else:
                        return
                else:
                    if abs(self.hp[cur_loc])>abs(self.hp[cur_child_L]):
                        self.hp[cur_loc],self.hp[cur_child_L]=self.hp[cur_child_L],self.hp[cur_loc]
                        cur_loc=cur_child_L
                    elif abs(self.hp[cur_loc])==abs(self.hp[cur_child_L]) and self.hp[cur_loc]>self.hp[cur_child_L]:
                        self.hp[cur_loc],self.hp[cur_child_L]=self.hp[cur_child_L],self.hp[cur_loc]
                        cur_loc=cur_child_L
                    else:
                        return

input = stdin.readline
N = int(input())
my_heap=make_heap()
Commands=[int(input()) for _ in range(N)]
for com in Commands:
    if not com:
        my_heap.root_pop()
    else:
        my_heap.push(com)
