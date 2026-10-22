# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next 
        
        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        rev = prev
        first = head

        while rev:
            first_next = first.next
            rev_next = rev.next

            rev.next = first.next
            first.next = rev

            rev = rev_next
            first = first_next



