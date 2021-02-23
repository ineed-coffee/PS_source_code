import sys
sys.setrecursionlimit(10**6)

def find(node):
    global parent

    if parent[node]==node:
        return node

    parent[node]=find(parent[node])
    return parent[node]

def union(node_a,node_b):
    global parent,rank
    head_a,head_b = find(node_a),find(node_b)

    if rank[head_a]>rank[head_b]:
        parent[head_b]=head_a
    else:
        parent[head_a]=head_b
        if rank[head_a]==rank[head_b]:
            rank[head_b]+=1
    return


if __name__ == "__main__" :

    input = sys.stdin.readline
    n,m = map(int,input().split())
    commands=[list(map(int,input().split())) for _ in range(m)]

    parent=[i for i in range(n+1)]
    rank=[0]*(n+1)

    for command,a,b in commands:
        if command==1:
            same = (find(a)==find(b))
            print("YES") if same else print("NO")
        elif command==0:
            if find(a)!=find(b):
                union(a,b)
