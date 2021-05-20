# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        
        if not root : return []
        
        que = deque([root])
        ret = []
        while que:
            tmp = []
            for _ in range(len(que)):
                cnode = que.popleft()
                tmp.append(cnode.val)
                if cnode.left: que.append(cnode.left)
                if cnode.right: que.append(cnode.right)
            ret.append(tmp)
            
        return ret
            
        
