# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(val=-1, next=head)
        count = 0
        HEAD = head
        while head:
            if count >= n:
                dummy = dummy.next
            head = head.next
            count += 1
        dummy.next = dummy.next.next
        if dummy.val == -1:
            return dummy.next
        else:
            return HEAD
