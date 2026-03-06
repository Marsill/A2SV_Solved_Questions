# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        has_cycle = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:         
                has_cycle = True
                break
            
        if not has_cycle:
            return None

        slow = head
        while slow != fast:      
            fast = fast.next
            slow = slow.next
        return slow
        
        
            