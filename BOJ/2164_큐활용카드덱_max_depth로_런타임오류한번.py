class Deck():
    def __init__(self,N):
        self.deck=[(i+1) for i in range(N)]
        self.L,self.R=0,N-1

    def push(self):
        self.deck.append(self.deck[self.L])
        self.R+=1
        
    def pop(self):
        if self.L<=self.R:
            self.L+=1

    def Solve(self):
        if self.L==self.R:
            print(self.deck[self.L])
            return
        else:
            while self.L!=self.R:
                self.pop()
                if self.L==self.R:
                    print(self.deck[self.L])
                    break
                else:
                    self.push()
                    self.pop()




N=int(input())
deck=Deck(N)
deck.Solve()
    
