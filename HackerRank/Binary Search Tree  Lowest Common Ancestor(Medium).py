# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
  #Enter your code here
  
    v1_anc,v2_anc=[],[]
  
    pointer=root
    depth=1
    while pointer.info!=v1:
        v1_anc.append((pointer,depth))
        if v1>pointer.info:
            pointer=pointer.right
        elif v1<pointer.info:
            pointer=pointer.left
        depth+=1
    if not v1_anc: return root
    v1_anc.append((pointer,depth))
  
    pointer=root
    depth=1
    while pointer.info!=v2:
        v2_anc.append((pointer,depth))
        if v2>pointer.info:
            pointer=pointer.right
        elif v2<pointer.info:
            pointer=pointer.left
        depth+=1
    if not v2_anc: return root
    v2_anc.append((pointer,depth))
    common_anc=set(v1_anc)&set(v2_anc)
    return sorted(list(common_anc),key=lambda x:x[1],reverse=True)[0][0]
