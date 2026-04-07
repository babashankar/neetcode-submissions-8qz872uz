# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(prev,head):
            if not head:
                return prev
            next=head.next
            head.next=prev
            return reverse(head,next)
        def shuffle(head1,head2):
            if not head1 or not head2:
                return head1 or head2
            
            next1,next2=head1.next,head2.next
            head1.next=head2
            head2.next=shuffle(next1,next2)
            return head1
        slow,fast=head,head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        nextOne=slow.next
        slow.next=None
        shuffle(head,reverse(None,nextOne))                   
        