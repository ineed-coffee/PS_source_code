# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        from collections import deque
        
        que=deque([root])
        
        while que:
            answer=0
            for _ in range(len(que)):
                cnode=que.popleft()
                answer+=cnode.val
                if cnode.left: que.append(cnode.left)
                if cnode.right: que.append(cnode.right)
        return answer
                
        
