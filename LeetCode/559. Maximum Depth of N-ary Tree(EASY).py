class Solution:
    def maxDepth(self, root: 'Node') -> int:
        from collections import deque
        if not root: return 0
                        
        que=deque([root])
        depth=0
        
        while que:
            depth+=1
            for _ in range(len(que)):
                current_node= que.popleft()
                for node in current_node.children:
                    que.append(node)
                
        return depth
