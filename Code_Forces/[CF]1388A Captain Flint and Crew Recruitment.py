import sys
 
input = sys.stdin.readline
 
t = int(input())
 
for case in range(t):
    n = int(input())
    if n<31:
        print('NO')
    else:
        print('YES')
        if n==36:
            Ans=[6,10,15,5]
        elif n==40:
            Ans=[6,10,15,9]
        elif n==44:
            Ans=[6,10,15,13]
        else:
            Ans=[6,10,14,n-30]
        print(*Ans)
