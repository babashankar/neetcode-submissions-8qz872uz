# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ahead=head
        while n:
            ahead=ahead.next
            n-=1
        curr=head

        prev=None
        while ahead:
            ahead=ahead.next
            prev=curr
            curr=curr.next
        if not prev:
            return head.next
        prev.next=curr.next
        return head 
            
        

        
        