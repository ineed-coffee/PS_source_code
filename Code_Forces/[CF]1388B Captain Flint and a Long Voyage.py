import sys
 
input = sys.stdin.readline
 
t = int(input())
 
for case in range(t):
    n = int(input())
    erased = n//4 + 1 if n%4 else n//4
    Ans = '9'*(n-erased)+'8'*(erased)
    print(int(Ans))
