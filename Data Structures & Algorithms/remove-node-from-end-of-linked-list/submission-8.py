# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #create a dummy node for the edge case that head is the node we want to delete
        dummy = ListNode(0, head)
        #initalize left to the dummy 
        left = dummy
        #initalize right to be one position right to the dummy 
        right = head 

        #move the right pointer n steps ahead so there are n node gaps
        while right and n > 0:
            #move the right pointer
            right = right.next
            #subtract n by 1 for the while loop condition
            n -=1
        
        #move the right pointer and left pointer until it points to Null at the end of the list so that the left pointer is the node before n 
        while right:
            #move left pointer forward
            left = left.next
            #move right forward
            right = right.next 
        #left pointer is now one before the node to delete 
        #delete the connection after left 
        left.next = left.next.next

        #time complexity is O(n) as this is the optimal one pass solution
        #memory complexity is O(1) as we only allocate variables left and right 
        
        return dummy.next