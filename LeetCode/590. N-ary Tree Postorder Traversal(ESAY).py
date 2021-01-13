"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        self.postorder=[]
        self.Post_Traversal(root)
        
        return self.postorder
    
    def Post_Traversal(self,node):
        
        if not node: return
        
        if node.children:
            for next_node in node.children:
                self.Post_Traversal(next_node)
        self.postorder.append(node.val)
        return
