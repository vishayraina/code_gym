# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node1 = ListNode(0, head)
        node2 = head
        count = 0
        remove_head = True
        while node2:
            if count >= n:
                node1 = node1.next
                remove_head = False
            node2 = node2.next
            count += 1
        if remove_head and head:
            head = head.next
        elif node1.next:
            node1.next = node1.next.next
        return head


