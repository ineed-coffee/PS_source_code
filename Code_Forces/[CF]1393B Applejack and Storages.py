import sys
 
input = sys.stdin.readline
 
n = int(input())
L = [*map(int,input().split())]
q = int(input())
events=[]
for _ in range(q):
    sym,num = input().rstrip().split()
    events.append([sym,int(num)])
 
L_dict={}
for l in L:
    try:
        L_dict[l]+=1
    except KeyError:
        L_dict[l]=1
 
double,quatro=0,0
for lth,cnt in L_dict.items():
    q_made=cnt//4
    d_made=(cnt%4)//2
    quatro+=q_made
    double+=d_made
    L_dict[lth]=[cnt,q_made,d_made]
    
for sym,num in events:
 
    if sym=='+':
 
        try:
            L_dict[num][0]+=1
            if (L_dict[num][0]//4)>L_dict[num][1]:
                L_dict[num][1]+=1
                L_dict[num][2]=0
                quatro+=1
                double-=1
            elif (L_dict[num][0]%4)//2>L_dict[num][2]:
                L_dict[num][2]+=1
                double+=1
 
        except KeyError:
            L_dict[num]=[1,0,0]
 
    else:
 
        L_dict[num][0]=max(0,L_dict[num][0]-1)
        if (L_dict[num][0]//4)<L_dict[num][1]:
            L_dict[num][1]-=1
            L_dict[num][2]+=1
            quatro-=1
            double+=1
        elif (L_dict[num][0]%4)//2<L_dict[num][2]:
            L_dict[num][2]-=1
            double-=1
    #print(f'double={double},quatro={quatro}')
    #print(L_dict)
    if (quatro>=2) or (quatro>=1 and double>=2):
        print('YES')
    else:
        print('NO')
    #print('--------------')
