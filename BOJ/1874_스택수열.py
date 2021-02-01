from sys import *

result=['+']
seq,stack=1,[1]
flag=True
N=int(input())
for _ in range(N):
    Num=int(stdin.readline())

    if flag:
        while True:
            if seq<Num:
                result.append('+')
                seq+=1
                stack.append(seq)
            else:
                if stack[-1]==Num:
                    result.append('-')
                    stack.pop()
                    break
                else:
                    flag=False
                    result=['NO']
                    break                

for r in result:
    print(r)
