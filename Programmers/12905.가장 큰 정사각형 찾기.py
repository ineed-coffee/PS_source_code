def solution(board):
    max_size = 1 if sum([sum(i) for i in board]) else 0
    R,C=len(board),len(board[0])
    for i in range(1,R):
        for j in range(1,C):
            if board[i][j]:
                board[i][j]=min(board[i-1][j],board[i][j-1],board[i-1][j-1])+1
                max_size=max(max_size,board[i][j])
    return max_size**2
