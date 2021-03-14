# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        L=0
        pointer=head
        while pointer:
            pointer=pointer.next
            L+=1
        
        from_head=None
        from_tail=None
        pointer=head
        idx=0
        while (from_head==None) or (from_tail==None):
            if idx==k-1:
                from_head=pointer
            if idx==L-k:
                from_tail=pointer
            idx+=1
            pointer=pointer.next
        
        from_head.val,from_tail.val=from_tail.val,from_head.val
        return head
