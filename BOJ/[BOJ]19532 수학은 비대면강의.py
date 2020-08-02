from sys import stdin

input = stdin.readline

a,b,c,d,e,f = map(int,input().split())

bottom = (a*e)-(b*d)
x=(e*c-b*f)/bottom
y=(a*f-c*d)/bottom
print(int(x),int(y))
