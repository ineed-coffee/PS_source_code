from sys import *

class Game():
    def __init__(self):
        self.A,self.B,self.C=0,0,0

    def Split(self,part,size):
        if size==1:
            if part[0][0]==-1:
                self.A+=1
            elif part[0][0]==0:
                self.B+=1
            elif part[0][0]==1:
                self.C+=1
        else:
            Flag=True
            Val=part[0][0]
            for i in range(size):
                for j in range(size):
                    if part[i][j]!= Val:
                        Flag=False;break
                    
            if Flag:
                if part[0][0]==-1:
                    self.A+=1
                elif part[0][0]==0:
                    self.B+=1
                elif part[0][0]==1:
                    self.C+=1
            else:
                size=size//3
                left=[l[:size] for l in part]
                mid=[m[size:2*size] for m in part]
                right=[r[2*size:] for r in part]
                part1=left[:size]
                part2=mid[:size]
                part3=right[:size]
                part4=left[size:2*size]
                part5=mid[size:2*size]
                part6=right[size:2*size]
                part7=left[2*size:]
                part8=mid[2*size:]
                part9=right[2*size:]
                self.Split(part1,size)
                self.Split(part2,size)
                self.Split(part3,size)
                self.Split(part4,size)
                self.Split(part5,size)
                self.Split(part6,size)
                self.Split(part7,size)
                self.Split(part8,size)
                self.Split(part9,size)


N=int(input())
sample=[list(map(int,stdin.readline().strip().split())) for _ in range(N)]
Board=Game()
Board.Split(sample,N)
print(Board.A)
print(Board.B)
print(Board.C)
'''
9
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
0 1 -1 0 1 -1 0 1 -1
0 -1 1 0 1 -1 0 1 -1
0 1 -1 1 0 -1 0 1 -1
'''
