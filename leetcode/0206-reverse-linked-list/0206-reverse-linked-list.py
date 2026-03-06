# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        temp = head
        
        while temp:
            arr.append(temp.val)
            temp = temp.next
        arr = arr[::-1]

        if not arr:
            return None
        
        new_head = ListNode(arr[0])
        curr = new_head
        for num in arr[1:]:
            curr.next = ListNode(num)
            curr = curr.next
        return new_head