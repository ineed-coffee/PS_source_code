# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        
        def backsum(node):
            nonlocal child_size
            
            if node not in child_size:
                child_size[node.val]=[0,0]
            
            if node.left:
                child_size[node.val][0]=backsum(node.left)
            if node.right:
                child_size[node.val][1]=backsum(node.right)
            
            return sum(child_size[node.val])+1
        
        child_size={}
        backsum(root)
        
        answer=[]
        stack=[(root,0)]
        possible=True
        while stack:
            cnode,cidx=stack.pop()
            
            if cnode.val!=voyage[cidx]:
                possible=False
                break
                
            L,R=child_size[cnode.val]
            
            if L and R:
                if (cnode.left.val==voyage[cidx+1]) and (cnode.right.val==voyage[cidx+1+L]):
                    stack.append((cnode.left,cidx+1))
                    stack.append((cnode.right,cidx+1+L))
                elif (cnode.right.val==voyage[cidx+1]) and (cnode.left.val==voyage[cidx+1+R]):
                    answer.append(cnode.val)
                    stack.append((cnode.right,cidx+1))
                    stack.append((cnode.left,cidx+1+R))
                else:
                    possible=False
                    break
            elif L:
                if cnode.left.val==voyage[cidx+1]:
                    stack.append((cnode.left,cidx+1))
                else:
                    possible=False
                    break
            elif R:
                if cnode.right.val==voyage[cidx+1]:
                    stack.append((cnode.right,cidx+1))
                else:
                    possible=False
                    break

        return answer if possible else [-1]
