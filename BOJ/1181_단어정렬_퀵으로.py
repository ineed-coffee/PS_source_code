from sys import *

def Solve(data): #using Quick-sort
    if len(data)<=1:
        return data
    
    r_list,l_list=[],[]
    pivot=data[0]
    for i in range(1,len(data)):
        if len(data[i]) < len(pivot):
            l_list.append(data[i])
        elif len(data[i]) == len(pivot):
            if data[i]< pivot:
                l_list.append(data[i])
            elif data[i]> pivot:
                r_list.append(data[i])
        else:
            r_list.append(data[i])
            
    l_list=Solve(l_list)
    r_list=Solve(r_list)
    return l_list+[pivot]+r_list

N = int(input())
data=[stdin.readline().strip() for i in range(N)]

for word in Solve(data):
    print(word)
