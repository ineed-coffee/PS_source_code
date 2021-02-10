import sys
from collections import defaultdict
sys.setrecursionlimit(10001)   
adj = defaultdict(dict)
routes=[]

def solution(tickets):
    global adj,routes
    
    for ticket in tickets:
        try:
            adj[ticket[0]][ticket[1]]+=1
        except KeyError:
            adj[ticket[0]] = defaultdict(int)
            adj[ticket[0]][ticket[1]]+=1
    
    T=len(tickets)
    start="ICN"
    backtrack(start,0,[start],T)
    routes.sort()
    return routes[0]

def backtrack(node,used_tickets,route,total_tickets):
    global adj,routes
    
    if used_tickets==total_tickets:
        routes.append(route)
        return
    
    for (k,v) in adj[node].items():
        if v:
            adj[node][k]-=1
            backtrack(k,used_tickets+1,route+[k],total_tickets)
            adj[node][k]+=1
    return
