class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        freq = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                current_num = matrix[i][j]
                if target == current_num:
                    return True
                
        else:
            return False