# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        L_ptr,R_ptr=None,None
        L_start,R_start=None,None
        cur=head
        while cur:
            if cur.val<x:
                if L_ptr==None:
                    L_ptr=cur
                    L_start=L_ptr
                else:
                    L_ptr.next=cur
                    L_ptr=L_ptr.next
                cur=cur.next
                L_ptr.next=None
            else:
                if R_ptr==None:
                    R_ptr=cur
                    R_start=R_ptr
                else:
                    R_ptr.next=cur
                    R_ptr=R_ptr.next
                cur=cur.next
                R_ptr.next=None
        
        if L_ptr and R_ptr:
            L_ptr.next=R_start
            return L_start
        elif not L_ptr:
            return R_start
        else:
            return L_start
        
