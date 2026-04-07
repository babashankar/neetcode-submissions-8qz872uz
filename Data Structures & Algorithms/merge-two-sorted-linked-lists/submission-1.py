# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def merge(head1,head2):
            if not head2 or not head1:
                return head1 or head2
            if head1.val<head2.val:
                head1.next=merge(head1.next,head2)
                return head1
            head2.next=merge(head1,head2.next)
            return head2
        return merge(list1,list2)
        