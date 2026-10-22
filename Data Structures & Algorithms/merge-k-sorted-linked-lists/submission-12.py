# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        

        def sortList(head):
            if head is None or head.next is None:
                return head
            slow = head
            fast = head.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            first_head = head
            second_head = slow.next
            slow.next = None 

            sorted_first = sortList(first_head)
            sorted_second = sortList(second_head)
            dummy_node = ListNode()
            curr = dummy_node

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
            return dummy_node.next 

        dummy_head = ListNode()
        curr = dummy_head

        for l in lists:
            curr.next = l
            while curr.next:
                curr = curr.next
           
      
        sorted_lists = sortList(dummy_head.next)
        return sorted_lists




