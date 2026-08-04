# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        slow.next = None
        
        
        prev = None
        while right:
            nxt = right.next
            right.next = prev
            prev = right
            right = nxt
        
        node1 = head
        node2 = prev
        while node1 and node2:
            nxt1 = node1.next
            nxt2 = node2.next
            node1.next = node2
            node2.next = nxt1
            node1 = nxt1
            node2 = nxt2

        return head

        
        