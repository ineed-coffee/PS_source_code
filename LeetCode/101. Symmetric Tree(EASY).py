# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        from collections import deque
        if not root : return True
        answer=True
        
        que = deque([root])
        
        while que:
            same_level=[]
            for _ in range(len(que)):
                current_node=que.popleft()
                if current_node.left:
                    que.append(current_node.left)
                    same_level.append(current_node.left.val)
                else:
                    same_level.append(None)
                
                if current_node.right:
                    que.append(current_node.right)
                    same_level.append(current_node.right.val)
                else:
                    same_level.append(None)

            if len(same_level)==1:
                continue
            mid = len(same_level)//2
            if not (all([same_level[i]==same_level[-i-1] for i in range(mid)])):
                answer=False
                break
        return answer
        
