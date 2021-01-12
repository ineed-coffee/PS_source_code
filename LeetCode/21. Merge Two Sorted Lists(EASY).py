# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        merged_head = None        
        current_l1=l1
        current_l2=l2
        
        while current_l1 or current_l2:
            
            if not current_l1:
                to_connect = current_l2
                current_l2 = current_l2.next
            
            elif not current_l2:
                to_connect = current_l1
                current_l1 = current_l1.next
            
            else:
                if current_l1.val >= current_l2.val:
                    to_connect = current_l2
                    current_l2 = current_l2.next
                else:
                    to_connect = current_l1
                    current_l1 = current_l1.next
                    
            if not merged_head:
                merged_head=to_connect
                merged_current = merged_head
            
            else:
                merged_current.next = to_connect
                merged_current = merged_current.next
            
        return merged_head
