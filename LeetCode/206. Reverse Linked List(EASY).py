# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution: # reversing iteratively
    def reverseList(self, head: ListNode) -> ListNode:
        current_node = head
        prev_node = None

        while current_node:
            
            tmp = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = tmp 
            
        return prev_node
