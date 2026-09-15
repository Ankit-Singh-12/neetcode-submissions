# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        vals = []

        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        
        n = len(vals)
        for i in range(0, n, k):
            if i + k <= n:
                vals[i: i + k] = vals[i : i + k][::-1]
        
        curr = head
        for val in vals:
            curr.val = val
            curr = curr.next
        
        return head