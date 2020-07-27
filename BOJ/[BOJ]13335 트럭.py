from sys import stdin
from collections import deque
input = stdin.readline

n,w,L = map(int,input().split())
weights = [*map(int,input().split())]
weights.reverse()

bridge = deque([0]*w)
br_w = 0
Ans = 0
passed = 0

while True:
#    print(bridge,br_w)
    head = bridge.popleft()
    if head:
        passed+=1
        br_w-=head

    if weights and weights[-1]+br_w <= L :
        tail = weights.pop()

    if tail:
        bridge.append(tail)
        br_w+=tail
        tail=0
    else:
        bridge.append(0)
    Ans+=1
    if passed == n:
        break

print(Ans)


# deque # data structure # simulation

