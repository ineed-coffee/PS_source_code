# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:return 0
        
        from collections import deque
        depth=0
        que=deque([root])
        
        while que:
            depth+=1
            for _ in range(len(que)):
                cur_node=que.popleft()
                if (not cur_node.left) and (not cur_node.right):
                    que=0
                    break
                if cur_node.left : que.append(cur_node.left)
                if cur_node.right : que.append(cur_node.right)
        return depth
        
        
        
