import sys
sys.setrecursionlimit(10**5)

def find(node):
    global parent

    if parent[node]==node:
        return node
    parent[node]=find(parent[node])
    return parent[node]

def union(node_a,node_b):
    global parent,rank,size
    head_a,head_b = find(node_a),find(node_b)

    if rank[head_a]>rank[head_b]:
        parent[head_b]=head_a
        size[head_a]+=size[head_b]
    else:
        parent[head_a]=head_b
        size[head_b]+=size[head_a]
        if rank[head_a]==rank[head_b]:
            rank[head_b]+=1
    return

if __name__ == "__main__" :
    
    input = sys.stdin.readline
    T = int(input().strip())

    for _ in range(T):
        F = int(input().strip())
        name_set=set([])
        name_to_idx={}
        parent=[]
        rank=[]
        size=[]

        for connection in range(F):
            #print("names :",name_set)
            #print("name to idx :",name_to_idx)
            #print("parent :",parent)
            #print("rank :",rank)
            #print("---------------")
            a,b = input().strip().split()

            if not a in name_set:
                name_set.add(a)
                name_to_idx[a]=len(parent)
                parent+=[len(parent)]
                rank+=[0]
                size+=[1]
            if not b in name_set:
                name_set.add(b)
                name_to_idx[b]=len(parent)
                parent+=[len(parent)]
                rank+=[0]
                size+=[1]

            if find(name_to_idx[a])!=find(name_to_idx[b]):
                union(name_to_idx[a],name_to_idx[b])

            print(size[find(name_to_idx[a])])
