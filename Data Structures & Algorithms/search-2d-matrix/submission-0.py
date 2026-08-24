class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        ROWS, COLS = len(matrix), len(matrix[0])
        low, high = 0, (ROWS * COLS) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Map the 1D index back to 2D coordinates
            row = mid // COLS
            col = mid % COLS
            
            guess = matrix[row][col]
            
            if guess == target:
                return True
            elif guess < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return False

        