from sys import stdin

input = stdin.readline

def treefy(po_lim,io_lim):
    po_s,po_e = po_lim
    io_s,io_e = io_lim

    if io_s>=io_e:
        if io_s==io_e:
            print(in_order[io_s],end=' ')
        return
        
    root = pre_order[po_s]
    r_idx = idx_pool[root]
    relative=r_idx-io_s

    l_po_s = po_s+1
    l_po_e = po_s+relative
    l_io_s = io_s
    l_io_e = r_idx-1

    r_po_s = po_s+relative+1
    r_po_e = po_e
    r_io_s = r_idx+1
    r_io_e = io_e

    treefy([l_po_s,l_po_e],[l_io_s,l_io_e])
    treefy([r_po_s,r_po_e],[r_io_s,r_io_e])
    print(root,end=' ')

T = int(input())
for case in range(T):
    n = int(input())
    pre_order = [*map(int,input().split())]
    in_order = [*map(int,input().split())]
    
    idx_pool = {}
    for i in range(n):
        idx_pool[in_order[i]]=i
    treefy([0,n-1],[0,n-1])
    print()

# tree # pre,in,post # div-conq
