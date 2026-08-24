# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node acts as the starting placeholder
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        # Continue loop if nodes exist or a carry remains
        while l1 or l2 or carry:
            # Extract values safely
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Compute total sum and new carry
            total = val1 + val2 + carry
            carry = total // 10
            
            # Append new node with the current digit
            curr.next = ListNode(total % 10)
            curr = curr.next
            
            # Advance input pointers if possible
            if l1: l1 = l1.next
            if l2: l2 = l2.next
                
        return dummy.next
