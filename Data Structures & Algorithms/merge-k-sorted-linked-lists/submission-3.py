# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge(head1,head2):
            if not head1 or not head2:
                return head1 or head2
            if head1.val<head2.val:
                head1.next=merge(head1.next,head2)
                return head1
            head2.next=merge(head1,head2.next)
            return head2
        while len(lists)>1:
            res=[]
            for i in range(0,len(lists),2):
                a=merge(lists[i],lists[i+1]) if i<len(lists)-1 else lists[i]
                res.append(a)
            lists=res
        return lists[0] if lists else None

        