# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #edge cases:
        if not head or not head.next:
            return  

        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        second_head = slow.next
        slow.next = None

        prev = None 

        while second_head:
            nxt = second_head.next
            second_head.next = prev
            prev = second_head
            second_head = nxt
        
        reverse_second_head = prev
        first = head

        while reverse_second_head:
            reverse_second_head_next = reverse_second_head.next
            first_next = first.next 

            reverse_second_head.next = first_next
            first.next = reverse_second_head

            #move each pointer forward
            reverse_second_head = reverse_second_head_next
            first = first_next

            

        