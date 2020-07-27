from sys import stdin
 
input = stdin.readline
 
T = int(input())
 
for case in range(T):
    n=int(input())
    a_list = [*map(int,input().split())]
    Ans = ['a'*60]
    for i in range(n):
        tmp = Ans[i][:a_list[i]]
        if a_list[i]>=len(Ans[i]):
            tmp2 = ''
        elif Ans[i][a_list[i]]=='b':
            tmp2 = 'a'*(60-a_list[i])
        else:
            tmp2 = 'b'*(60-a_list[i])
        tmp+=tmp2
        Ans.append(tmp)
 
    for row in Ans:
        print(row)
