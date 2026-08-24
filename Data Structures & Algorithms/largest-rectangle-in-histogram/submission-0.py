class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = 0
        stack = []  # Pairs of (index, height)
        
        for i, h in enumerate(heights):
            start = i
            # Pop bars that are taller than the current bar
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                # The current smaller bar can extend backwards to the popped bar's index
                start = idx
            stack.append((start, h))
            
        # Process remaining bars in the stack extending to the end of the histogram
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
            
        return max_area
