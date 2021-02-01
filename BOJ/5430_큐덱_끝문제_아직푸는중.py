from sys import *
import re


class ARR():
    def __init__(self,sample,size):
        self.out=sample[:]
        self.size=size

    def R(self):
        if self.size>1:
            for i in range(self.size//2):
                self.out[i],self.out[self.size-1-i]=self.out[self.size-1-i],self.out[i]
        return
    
    def D(self):
        if self.size:
            self.out.pop(0)
            self.size-=1
            return
        else:
            self.out='error'
            return



test_case=int(input())
for _ in range(test_case):
    Commands=list(str(stdin.readline().strip()))
    Size=int(stdin.readline().strip())
#    Sample=stdin.readline().strip().split(',')
    Sample=stdin.readline().strip()
    Sample=re.split("\[|,|\]",Sample)
    print(Sample)
'''    Sample[0]=str(list(Sample[0])[1:])
    Sample[-1]=str(list(Sample[-1])[:-1])
    Deck=ARR(Sample,Size)
    for com in Commands:
        if com=='R':
            Deck.R()
        elif com=='D' :
            Deck.D()
        if Deck.out=='error':
            break
    print(Deck.out)
'''
    
