import sys

def get_failure_func(pattern):

    return_list=[0]

    for i in range(1,len(pattern)):
        j=return_list[i-1]

        while j>0 and pattern[j]!=pattern[i]:
            j = return_list[j-1]

        return_list.append(j+1 if pattern[j]==pattern[i] else j)

    return return_list

def kmp_search(S,P):
    return_list=[]
    ff = get_failure_func(P)
    j=0
    for i in range(len(S)):

        while j>0 and S[i]!=P[j]:
            j=ff[j-1]
        if S[i]==P[j]:
            j+=1
        if j==len(P):
            return_list.append(i-j+2)
            j=ff[j-1]

    return return_list

if __name__ == '__main__':
    input=sys.stdin.readline
    T = input().rstrip()
    P = input().rstrip()
    Ans=kmp_search(T,P)
    if not len(Ans):
        print(0)
    else:
        print(len(Ans))
        print(*Ans)
        
    #print(*get_failure_func(P))
