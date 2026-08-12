class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = (rows*cols)-1
        while left <= right:
            mid = (left+right)//2
            row = mid//cols
            col = mid%cols
            mid_number = matrix[row][col]

            if target == mid_number:
                return True
            
            elif target < mid_number:
                right = mid - 1

            elif target > mid_number: 
                left = mid + 1
        return False