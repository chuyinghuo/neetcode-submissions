# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #edge cases:
        if head is None or head.next is None:
            return head

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        first_half = head
        slow.next = None

        second_half_head = self.sortList(second_half)
        first_half_head = self.sortList(first_half)

        dummy_node = ListNode()
        curr = dummy_node

        while second_half_head and first_half_head:
            if first_half_head.val <= second_half_head.val:
                curr.next = first_half_head
                first_half_head = first_half_head.next

            elif second_half_head.val < first_half_head.val:
                curr.next = second_half_head
                second_half_head = second_half_head.next
            curr = curr.next
        curr.next = second_half_head or first_half_head
        return dummy_node.next
