def Quick_sort(data):
    if len(data)<=1:
        return data
    
    r_list,l_list=[],[]
    pivot=data[0]
    for i in range(1,len(data)):
        if data[i]> pivot:
            l_list.append(data[i])
        else:
            r_list.append(data[i])
    l_list=Quick_sort(l_list)
    r_list=Quick_sort(r_list)
    return l_list+[pivot]+r_list

N = input()
Desc_list=list(map(int,N))

for element in Quick_sort(Desc_list):
    print(element,end='')
