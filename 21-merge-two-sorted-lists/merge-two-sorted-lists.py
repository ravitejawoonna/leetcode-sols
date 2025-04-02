# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = current = ListNode(0)

        while l1 and l2:

            if l1.val >= l2.val:
                current.next = l2
                l2 = l2.next
            else:
                current.next = l1
                l1 = l1.next
            current = current.next
        
        if l1:
            while l1:
                current.next = l1
                l1 = l1.next
                current = current.next
        if l2:
            while l2:
                current.next = l2
                l2 = l2.next
                current = current.next
        
        return head.next