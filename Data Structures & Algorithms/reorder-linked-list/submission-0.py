# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Find the middle of the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # second half starts after slow pointer
        second = slow.next
        slow.next = None  # Split the list into two halves

        # 2. Reverse the second half
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
            
        # 3. Merge the two halves alternatingly
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
