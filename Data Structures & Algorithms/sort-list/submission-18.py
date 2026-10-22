# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_head = slow.next
        first_head = head
        slow.next = None
        
        sorted_first = self.sortList(first_head)
        sorted_second = self.sortList(second_head)

        dummy_head = ListNode()
        curr = dummy_head

        while sorted_first and sorted_second:
            if sorted_first.val <= sorted_second.val:
                curr.next = sorted_first
                sorted_first = sorted_first.next
            else:
                curr.next = sorted_second
                sorted_second = sorted_second.next 
            curr = curr.next 
        if sorted_first:
            curr.next = sorted_first
        elif sorted_second:
            curr.next = sorted_second
        return dummy_head.next






