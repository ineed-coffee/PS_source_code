# BFS-----------------------------------
class Solution:
    def getImportance(self, employees: List['Employee'], id_: int) -> int:
        from collections import deque
        
        def dictionize(arr):
            return {"importance":arr.importance,"subordinates":arr.subordinates}
        
        employees = {info.id:dictionize(info) for info in employees}
        
        que = deque([id_])
        total_imp=0
        while que:
            current_emp = que.popleft()
            total_imp+=employees[current_emp]["importance"]
            for sub in employees[current_emp]["subordinates"]:
                que.append(sub)

        return total_imp

# DFS-----------------------------------
class Solution:
    def getImportance(self, employees: List['Employee'], id_: int) -> int:
        
        def dictionize(arr):
            return {"importance":arr.importance,"subordinates":arr.subordinates}
        
        employees = {info.id:dictionize(info) for info in employees}
        
        stack = [id_]
        total_imp=0
        while stack:
            current_emp = stack.pop()
            total_imp+=employees[current_emp]["importance"]
            for sub in employees[current_emp]["subordinates"]:
                stack.append(sub)

        return total_imp
