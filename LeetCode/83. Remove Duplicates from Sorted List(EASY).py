# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        current_node = head
        
        while current_node:
            
            current_val = current_node.val
            tmp=current_node.next
            while tmp:
                if tmp.val!=current_val:
                    break
                
                to_delete = tmp
                tmp = tmp.next
                del to_delete
                
            current_node.next = tmp
            current_node = current_node.next
      
        return head
