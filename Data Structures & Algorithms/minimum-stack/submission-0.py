class MinStack:

    def __init__(self):
        # The main stack stores all elements
        self.stack = []
        # The min_stack stores the minimums corresponding to each state
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Determine the current minimum to push onto the min_stack
        if self.min_stack:
            current_min = min(val, self.min_stack[-1])
        else:
            current_min = val
        self.min_stack.append(current_min)

    def pop(self) -> None:
        # Both stacks must stay synchronized
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        # Return the top element of the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the top element of the min stack
        return self.min_stack[-1]
