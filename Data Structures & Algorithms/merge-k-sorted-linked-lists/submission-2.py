# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None

        def merge(head1,head2):
            if not head1:
                return head2
            if not head2:
                return head1
            if head1.val<head2.val:
                head1.next=merge(head1.next,head2)
                return head1
            else:
                head2.next=merge(head1,head2.next)
                return head2

        res=[]

        

        while len(lists)>1:
            l=len(lists)
            tmp=[]


            for i in range(0,l,2):
                tmp.append(merge(lists[i],lists[i+1]) if i+1<l else lists[i])
            lists=tmp
        return lists[0]

        