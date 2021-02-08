# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        
        if not root:return []
        
        que1 = deque([root])
        que2 = deque([[root.val]])
        
        while que1:
            tmp=[]
            for _ in range(len(que1)):
                current_node = que1.popleft()
                if current_node.left:
                    que1.append(current_node.left)
                    tmp.append(current_node.left.val)
                if current_node.right:
                    que1.append(current_node.right)
                    tmp.append(current_node.right.val)
            if tmp:
                que2.appendleft(tmp)
        return list(que2)
