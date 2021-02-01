from sys import stdin

def A1(data):
    return int(round(sum(data)/len(data)))

def A2(mode):
    temp = []
    for i in sorted(mode):
        for j in range(mode[i]):
            temp.append(i)
    return temp[sum(mode.values())//2]

def A3(mode):
    temp=[]
    for i in mode:
        if mode[i]==max(mode.values()): temp.append(i)
    if len(temp)>1:return sorted(temp)[1]
    else:return temp[0]

def A4(mode):
    if len(mode.keys())==1:return 0
    else: return sorted(mode)[-1]-sorted(mode)[0]
    
N=int(input())
Mode_dict={}
data_list=[]
for i in range(N):
    element=int(stdin.readline())
    data_list.append(element)
    try:
        Mode_dict[element]+=1
    except KeyError:
        Mode_dict[element]=1
    
print(A1(data_list))
print(A2(Mode_dict))
print(A3(Mode_dict))
print(A4(Mode_dict))
