# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        bin_str = ""
        
        current_node = head
        
        while current_node:
            bin_str+=str(current_node.val)
            current_node = current_node.next

        bin_str = "0b"+bin_str
        return int(bin_str,2)
