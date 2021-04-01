# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def isPalindrome(self, head: ListNode) -> bool:
        ret=[]
        node=head
        while node:
            ret.append(node.val)
            node=node.next
        
        L,R=0,len(ret)-1
        while L<R:
            if ret[L]!=ret[R]:
                return False
            L+=1
            R-=1
        return True
