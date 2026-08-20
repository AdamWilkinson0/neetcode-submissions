# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        s = head
        f = head

        while f and f.next:
            if f.next.next != None and s.next != None:
                s = s.next
                f = f.next.next
            else:
                return False
            if s == f:
                return True
            

        return False
