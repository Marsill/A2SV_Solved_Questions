# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:  
            while stack and head.val > stack[-1].val:
                stack.pop()

            stack.append(head)
            head = head.next

        h = ListNode()
        dummy = ListNode()
        dummy = h
        h.next = stack[0]
        for i in range(1, len(stack)):  
            h = h.next      
            h.next = stack[i]
        return dummy.next
