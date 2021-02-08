# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        from collections import deque
        
        if root.val in [x,y] : return False
        
        parents=[]
        que=deque([root])
        depth=0
        
        while que:
            depth+=1
            
            for _ in range(len(que)):
                current_node = que.popleft()

                if current_node.left:
                    que.append(current_node.left)
                    if current_node.left.val in [x,y]:
                        parents.append((current_node.val,depth))
                if current_node.right:
                    que.append(current_node.right)
                    if current_node.right.val in [x,y]:
                        parents.append((current_node.val,depth))
        
        if parents[0][1]!=parents[1][1]:
            return False
        elif parents[0][0]==parents[1][0]:
            return False
        else:
            return True
        
