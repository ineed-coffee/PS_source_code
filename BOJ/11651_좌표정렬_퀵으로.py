from sys import *

def Quick_sort(data):
    if len(data)<=1:
        return data
    
    r_list,l_list=[],[]
    pivot=data[0]
    for i in range(1,len(data)):
        if data[i][1]< pivot[1]:
            l_list.append(data[i])
        elif data[i][1]== pivot[1]:
            if data[i][0]< pivot[0]:
                l_list.append(data[i])
            else:
                r_list.append(data[i])
        else:
            r_list.append(data[i])
            
    l_list=Quick_sort(l_list)
    r_list=Quick_sort(r_list)
    return l_list+[pivot]+r_list

N = int(input())
data=[list(map(int,stdin.readline().split())) for i in range(N)]

for cord in Quick_sort(data):
    print(cord[0],cord[1])
