# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pointer_A=headA
        node_visited=set()
        
        while pointer_A:
            node_visited.add(pointer_A)
            pointer_A=pointer_A.next
            
        Answer=None
        pointer_B=headB
        while pointer_B:
            if pointer_B in node_visited:
                Answer=pointer_B
                break
            pointer_B=pointer_B.next
            
        return Answer
        
        
        
        
        
