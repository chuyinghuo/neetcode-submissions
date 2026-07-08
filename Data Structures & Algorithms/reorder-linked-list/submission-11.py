# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return 
       
        copy = []
        cur = head

        while cur:
            copy.append(cur)
            cur = cur.next 

        i, j = 0, len(copy)-1
        while i < j:
            copy[i].next = copy[j]
            i += 1
            if i>= j:
                break 
            copy[j].next = copy[i]
            j -= 1
        copy[i].next = None




        
