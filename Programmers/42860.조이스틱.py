def solution(name):
    moves=0
    not_a,L=[],len(name)
    for i,letter in enumerate(name):
        if letter!="A":
            not_a.append(i)
        moves+=min(abs(ord("A")-ord(letter)),1+abs(ord("Z")-ord(letter)))

    def keygen(cur,x,l):
        if abs(cur-x)<=L-abs(cur-x):
            return (abs(cur-x) , -1)
        return (L-abs(cur-x),1)

    cursor=0
    while not_a:
        not_a.sort(key=lambda x:keygen(x,cursor,L),reverse=True)
        next_cursor=not_a.pop()
        moves+=min(abs(cursor-next_cursor),L-abs(cursor-next_cursor))
        cursor=next_cursor

    return moves
