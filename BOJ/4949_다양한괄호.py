from sys import *

line_result=[]
left,right=['(','['],[')',']']
ending=['.']
while True:
    sample=list(str(stdin.readline().rstrip()))
    if sample == ending:
        break
    else:
        temp=[]
        flag=True
        for element in sample:
            if element in left:
                temp.append(element)
            elif element in right:
                if temp:
                    if element==')' and temp[-1]=='(':
                        temp.pop()
                    elif element==']' and temp[-1]=='[' :
                        temp.pop()
                    else:
                        flag=False
                        break
                else:
                    flag=False
                    break
        line_result.append('yes' if flag and not temp else 'no')

for line in line_result:
    print(line)
