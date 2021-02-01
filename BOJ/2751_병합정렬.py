import sys

def Solve(data):
    if len(data)<=1:
        return data
    else:
        center=len(data)//2
        L=Solve(data[:center])
        R=Solve(data[center:])
        return Merge(L,R)

def Merge(L,R):
    i,j,temp_list=0,0,[]

    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            temp_list.append(L[i])
            i+=1
        elif L[i]>R[j]:
            temp_list.append(R[j])
            j+=1
    while i<len(L):
        temp_list.append(L[i])
        i+=1
    while j<len(R):
        temp_list.append(R[j])
        j+=1
    return temp_list

    

N=int(input())
data=[]
for i in range(N):
    data.append(int(sys.stdin.readline().strip()))
for i in Solve(data):
    print(i)
