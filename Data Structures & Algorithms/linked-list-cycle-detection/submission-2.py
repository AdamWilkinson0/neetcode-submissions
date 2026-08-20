# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        alreadyVisited = set()

        curr = head
        while curr:
            alreadyVisited.add(curr)
            if curr.next != None:
                if curr.next in alreadyVisited:
                    return True
                else:
                    curr = curr.next
            else:
                return False
        return False
