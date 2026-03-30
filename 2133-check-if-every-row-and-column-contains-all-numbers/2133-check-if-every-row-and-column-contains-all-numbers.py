class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)
        
        # Kiểm tra từng hàng
        for row in matrix:
            if set(row) != set(range(1, n + 1)):
                return False
        
        # Kiểm tra từng cột
        for col in range(n):
            column = [matrix[row][col] for row in range(n)]
            if set(column) != set(range(1, n + 1)):
                return False
        
        return True
