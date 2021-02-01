from sys import *

def Short_code(S):
    if len(S)==1:
        return S
    else:
        Conc=[None]*len(S)
        S_=[]
        Out=''
        Always_false=False
        for i in range(len(S)):
            if '==' in S[i]:
                Conc[i]=0
                temp_1,temp_2 = S[i].split('==')
                S_.append([temp_1,temp_2] if len(temp_1)<len(temp_2) else [temp_2,temp_1])
            elif '!=' in S[i]:
                
                Conc[i]=1
                temp_1,temp_2 = S[i].split('!=')
                S_.append([temp_1,temp_2] if len(temp_1)<len(temp_2) else [temp_2,temp_1])
        for j in range(len(S)):
            if Always_false:
                break
            for k in range(len(S)):
                if j!=k and Conc[j]!=2:
                    if S_[j][1] in S_[k]:
                        if S_[j][0] in S_[k]:
                            if Conc[j]==Conc[k]:
                                Conc[k]=2
                            else:
                                Always_false=True
                                break
                        elif S_[j][1] == S_[k][0] and Conc[j]==0 :
                            S_[k][0]= S_[j][0] if len(S_[j][1])>=len(S_[j][0]) else S_[k][0]
                        elif S_[j][1] == S_[k][1] and Conc[j]==0 :
                            S_[k][1]= S_[j][0] if len(S_[j][1])>=len(S_[j][0]) else S_[k][1]
        if Always_false:
            Out='0==1'
        else:
            for l in range(len(S)):
                if Conc[l]==0:
                    Out+='=='.join(S_[l])
                elif Conc[l]==1:
                    Out+='!='.join(S_[l])
        
                if l!=len(S)-1:
                    Out+='&&'
            Out=Out[:-2] if Out[-2:]=='&&' else Out
            
        return Out
    
S= stdin.readline().strip().split('&&')

print(Short_code(S))

