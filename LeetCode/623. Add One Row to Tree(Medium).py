# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        
        if d==1:
            new_root=TreeNode(val=v)
            new_root.left=root
            return new_root
            
        level_d_1=[]

        stack=[(root,1)]
        while stack:
            cur_node,cur_depth=stack.pop()
            if cur_depth==d-1:
                level_d_1.append(cur_node)
                continue
            if cur_node.left:
                stack.append((cur_node.left,cur_depth+1))
            if cur_node.right:
                stack.append((cur_node.right,cur_depth+1))

        while level_d_1:
            cur_node=level_d_1.pop()
            og_left,og_right=cur_node.left,cur_node.right
            cur_node.left,cur_node.right=TreeNode(val=v),TreeNode(val=v)
            cur_node.left.left=og_left
            cur_node.right.right=og_right
        return root            
