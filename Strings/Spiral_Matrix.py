class Solution:
    def spiralOrder(self, matrix):

        final_list = []

        top = 0
        bottom = len(matrix)-1
        right = len(matrix[0])-1
        left = 0

        #Traversing the first row from left to right
        while top <= bottom and left <= right:

            for j in range(left, right+1):
                final_list.append(matrix[top][j])
            top += 1

            #Traversing from the top row to the bottom row

            for i in range(top, bottom+1):
                final_list.append(matrix[i][right])
            right -= 1

            #Traversing from the right to the left
            if left <= right:
                for j in range(right, left-1, -1):
                    final_list.append(matrix[bottom][j])
                bottom -= 1

            #Traversing from the bottom the the top again
            if top <= bottom:
                for i in range(bottom, top-1, -1):
                    final_list.append(matrix[i][left])
                left += 1

        print(final_list)

        return final_list
    
solution = Solution()
matrix1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# matrix2 = [[1,2],[3,4]]
solution.spiralOrder(matrix1)
# solution.spiralOrder(matrix2)