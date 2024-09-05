class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        first_row_zero = False
        first_column_zero = False

        for i in range(row):
            if matrix[i][0] == 0:
                first_column_zero = True

        for j in range(col):
            if matrix[0][j] == 0:
                first_row_zero = True
        

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_column_zero:
            for i in range(row):
                matrix[i][0] = 0
        
        if first_row_zero:
            for j in range(col):
                matrix[0][j] = 0
        
        # print(matrix)
        

        return matrix
    
Solution = Solution()
matrix = [[1,2,3,0],[4,5,6,0],[7,8,9,0]]
Solution.setZeroes(matrix)