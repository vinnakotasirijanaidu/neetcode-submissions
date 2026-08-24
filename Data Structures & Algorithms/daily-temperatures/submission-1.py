class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # stores pairs of [temperature, index]
        
        for i, t in enumerate(temperatures):
            # Check if current temp is warmer than the temp at the top of the stack
            while stack and t > stack[-1][0]:
                stack_t, stack_i = stack.pop()
                res[stack_i] = i - stack_i
                
            stack.append([t, i])
            
        return res
