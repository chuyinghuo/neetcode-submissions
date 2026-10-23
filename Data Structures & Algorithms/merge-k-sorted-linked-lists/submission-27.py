# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None


        def mergeList(l1, l2):
            
            head_one = l1
            head_two = l2

            dummy = ListNode()
            curr = dummy 
            while head_one and head_two:
                if head_one.val <= head_two.val:
                    curr.next = head_one
                    head_one = head_one.next
                else:
                    curr.next = head_two
                    head_two = head_two.next
                curr = curr.next 
            curr.next = head_one or head_two 
            return dummy.next

       
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                if (i+1) < len(lists):
                    l2 = lists[i+1]
                else:
                    l2 = None 
                
                merged.append(mergeList(l1, l2))
            lists = merged
        return lists[0]

        


            




