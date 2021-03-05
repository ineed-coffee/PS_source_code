# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        from collections import deque
        
        answer=[]
        que=deque([root])
        while que:
            cur_avg,L=0,len(que)
            for _ in range(L):
                cur_node=que.popleft()
                cur_avg+=cur_node.val
                if cur_node.left: que.append(cur_node.left)
                if cur_node.right: que.append(cur_node.right)
            answer.append(cur_avg/L)
        return answer
        
