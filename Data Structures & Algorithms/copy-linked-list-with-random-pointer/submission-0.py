class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        # Hash map to map old nodes to their deep copies
        old_to_new = {}
        
        # Step 1: Create copies of all nodes and store them in the map
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
            
        # Step 2: Assign next and random pointers for the copied nodes
        curr = head
        while curr:
            # If curr.next is None, old_to_new.get(None) returns None
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next
            
        # Return the head of the newly created copied list
        return old_to_new[head]
