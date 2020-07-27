import sys

input = sys.stdin.readline

t = int(input())

for case in range(t):
    n = int(input())
    A_str = input().rstrip()
    B_str = input().rstrip()

    flag=True
    Trans_set = [set() for _ in range(20)]
    for i in range(n):
        if B_str[i]<A_str[i]:
            flag=False
            break
        elif A_str[i]!=B_str[i]:
            Trans_set[ord(A_str[i])-97].add(B_str[i])

    Ans=-1
    if flag:
        Ans=0
        for i in range(20):
            if not Trans_set[i]:
                continue
            tmp=Trans_set[i]
            nxt = min(list(tmp))
            tmp.remove(nxt)
            Trans_set[ord(nxt)-97].update(list(tmp))
            Ans+=1

    print(Ans)
