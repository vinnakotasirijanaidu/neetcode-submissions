import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # Define the search space for the eating speed k
        left = 1
        right = max(piles)
        
        # Result variable to store the minimum valid speed found
        result = right
        
        while left <= right:
            mid = (left + right) // 2
            
            # Calculate total hours needed with eating speed 'mid'
            total_hours = 0
            for pile in piles:
                total_hours += (pile + mid - 1) // mid
            
            # If Koko can finish within h hours, try to find a smaller speed
            if total_hours <= h:
                result = mid
                right = mid - 1
            else:
                # If it takes too long, increase the speed
                left = mid + 1
                
        return result
