# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(prev,head):
            if head==None:
                return prev
            next=head.next
            head.next=prev
            return reverse(head,next)
        return reverse(None,head)
            
        