import sys
 
input = sys.stdin.readline
 
T = int(input())
 
for case in range(T):
    n = int(input())
    print(1+(n//2))
