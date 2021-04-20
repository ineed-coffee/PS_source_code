"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# Recursive way
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        if not root: return []

        def pre_trav(node):
            order_=[node.val]
            if node.children:
                for nxt in node.children:
                    order_+=pre_trav(nxt)
            return order_
        
        return pre_trav(root)

# Iterable way
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        if not root: return []

        answer=[]
        stack=[root]
        while stack:
            node=stack.pop()
            answer.append(node.val)
            
            ch=node.children
            stack = stack if not ch else stack+ch[::-1]

        return answer
