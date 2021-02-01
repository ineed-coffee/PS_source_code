from sys import *

class Game():
    def __init__(self):
        self.blue,self.white=0,0

    def Split(self,part,size):
        if size==1:
            if part[0][0]==1:
                self.blue+=1
            elif part[0][0]==0:
                self.white+=1
        else:
            Sum=0
            for i in range(size):
                Sum+=sum(part[i])
                    
            if Sum==0 or Sum==size*size:
                if part[0][0]==1:
                    self.blue+=1
                elif part[0][0]==0:
                    self.white+=1
            else:
                size=size//2
                left=[l[:size] for l in part]
                right=[r[size:] for r in part]
                part1=left[:size]
                part2=right[:size]
                part3=left[size:]
                part4=right[size:]
                self.Split(part1,size)
                self.Split(part2,size)
                self.Split(part3,size)
                self.Split(part4,size)


N=int(input())
sample=[list(map(int,stdin.readline().strip().split())) for _ in range(N)]
Board=Game()
Board.Split(sample,N)
print(Board.white)
print(Board.blue)
'''
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1
'''
