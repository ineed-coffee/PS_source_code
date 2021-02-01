class Solution:
    def totalMoney(self, n: int) -> int:
        
        balance = 0
        weeks,days = n//7,n%7
        for week in range(weeks):
            balance+=(7*8)//2 + 7*week
        balance += (days*(days+1))//2 + days*(weeks)
        return balance
