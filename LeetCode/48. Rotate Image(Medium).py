class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N=len(matrix)
        iter_=(N//2)
        switch=[N-1,N-1,N-1,N]
        for idx in range(iter_):
            store = [[idx,i,matrix[idx][i]] for i in range(idx,N-1-idx)]
            L=N-1-(2*idx)
            for rotate in range(4):
                for i in range(L):
                    x,y,val = store[i]
                    update=matrix[y][switch[rotate]-x]
                    matrix[y][N-1-x]=val
                    store[i]=[y,N-1-x,update]
        return
