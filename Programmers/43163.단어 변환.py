def solution(begin, target, words):
    if target not in words: return 0
    
    from collections import deque
    word_bag=[begin]+words
    target_idx=word_bag.index(target)
    N = len(word_bag)
    
    dist={i:[] for i in range(N)}
    for i in range(N):
        for j in range(N):
            letter_check=[i!=j for (i,j) in zip(word_bag[i],word_bag[j])]
            if sum(letter_check)<=1:
                dist[i].append(j)
    
    moves = 0
    visited=[False]*N
    que=deque([0])
    while que:
        moves+=1
        for _ in range(len(que)):
            current_node = que.popleft()
            visited[current_node]=True
            for next_node in dist[current_node]:
                if not visited[next_node]:
                    if next_node==target_idx:
                        return moves
                    que.append(next_node)
    
    return 0
