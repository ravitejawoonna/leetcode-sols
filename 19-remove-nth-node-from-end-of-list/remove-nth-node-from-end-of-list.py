# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head

        for _ in range(n):
            fast = fast.next
        
        while fast and fast.next: # need to go to the last node of list
            slow = slow.next
            fast = fast.next
        
        if not fast:
            return head.next
        
        slow.next = slow.next.next
        return head