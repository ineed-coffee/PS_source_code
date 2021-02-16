def solution(n, costs):
    answer = 0
    
    parent=[i for i in range(n)]
    rank = [0]*n
    costs.sort(key=lambda x:x[-1])
    
    for (node1,node2,weight) in costs:
        if find(node1,parent)!=find(node2,parent):
            union(node1,node2,parent,rank)
            answer+=weight
    return answer

def find(node,parent):
    if parent[node]==node:
        return node
    parent[node]=find(parent[node],parent)
    return parent[node]

def union(node_a,node_b,parent,rank):
    head_a,head_b=find(node_a,parent),find(node_b,parent)
    if rank[head_a]>rank[head_b]:
        parent[head_b]=head_a
    else:
        if rank[head_a]==rank[head_b]:
            rank[head_b]+=1
        parent[head_a]=head_b
    return
