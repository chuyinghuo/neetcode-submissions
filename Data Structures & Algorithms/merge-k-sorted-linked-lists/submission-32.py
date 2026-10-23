# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeList(l1, l2):
            dummy = ListNode()
            curr = dummy 
            first = l1
            second = l2

            while first and second:
                if first.val <= second.val:
                    curr.next = first
                    first = first.next 
                else:
                    curr.next = second
                    second = second.next 
                curr = curr.next 
            curr.next = first or second 
            return dummy.next

        if not lists:
            return None

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
                

        