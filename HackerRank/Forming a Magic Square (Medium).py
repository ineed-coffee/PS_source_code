from sys import stdin

def rotate(mat):

    return flip(list(map(list,zip(*mat))))

def flip(mat):
    tmp =[]
    for row in mat:
        tmp.append(list(reversed(row)))
    return tmp

def comp(mat,magic):
    ret = 0

    for i in range(3):
        for j in range(3):
            ret+=abs(mat[i][j]-magic[i][j])
    return ret

if __name__ == '__main__':
    
    input = stdin.readline

    Mat = [[*map(int,input().split())] for _ in range(3)]

    Ans=10**6

    Magic = [[4,9,2],[3,5,7],[8,1,6]]

    for i in range(8):
        if i:
            Magic = rotate(Magic)
            if i==4:
                Magic = flip(Magic)
#        for row in Magic:
#            print(row)
#        print('##')
        Ans = min(Ans,comp(Mat,Magic))

    print(Ans)




'''


4 9 2
3 5 7
8 1 6
'''
