# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node_list=[]
        node=head
        while node:
            node_list.append(node)
            node=node.next
            
        if node_list[-n]!=node_list[0]:
            prev=node_list[-(n+1)]
            nxt=prev.next.next
            prev.next.next=None
            prev.next=nxt
            return head
        else:
            tmp=head.next
            head.next=None
            return tmp
        
        
