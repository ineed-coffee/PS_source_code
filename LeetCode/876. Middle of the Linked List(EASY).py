# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        Len = 0
        self.current_node = head
        
        while self.current_node:
            Len+=1
            self.current_node = self.current_node.next
            
        Mid = (Len//2)+1
        
        self.current_node = head
        while Mid>1:
            self.current_node = self.current_node.next
            Mid-=1
            
        return self.current_node
