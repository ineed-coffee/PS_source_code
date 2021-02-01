def Bubble_sort(data):
    for i in range(len(data)-1):
        swap=0
        for j in reversed(range(i+1,len(data))):
            if data[j]>data[j-1]:
                data[j],data[j-1] = data[j-1],data[j]
                swap+=1
        if swap ==0:
            break
        
    for k in data:
        print(k,end='')


N = input()
Desc_list=list(map(int,N))

Bubble_sort(Desc_list)

