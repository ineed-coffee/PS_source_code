from sys import stdin
 
input = stdin.readline
 
T = int(input())
for case in range(T):
    x,y,z = map(int,input().split())
 
    if x==y and y==z:
        print('YES')
        print(x,x,x)
    elif y==z and x<y:
        print('YES')
        print(x,x,y)
    elif x==y and y>z:
        print('YES')
        print(x,z,z)
    elif x==z and y<z:
        print('YES')
        print(y,y,z)
    else:
        print('NO')
