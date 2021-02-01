from sys import *

def Solve(data): #using Quick-sort
    if len(data)<=1:
        return data
    
    r_list,l_list=[],[]
    pivot=data[0]
    for i in range(1,len(data)):
        if data[i][0] < pivot[0]:
            l_list.append(data[i])
        elif data[i][0] == pivot[0]:
            if data[i][2] < pivot[2]:
                l_list.append(data[i])
            else:
                r_list.append(data[i])
        else:
            r_list.append(data[i])
            
    l_list=Solve(l_list)
    r_list=Solve(r_list)
    return l_list+[pivot]+r_list

N = int(input())
data=[]
for _ in range(N):
    age,name=stdin.readline().strip().split()
    data.append([int(age),name,_])
    
for order in Solve(data):
    print(order[0],order[1])
