"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix.
This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
"""


class Solution:
    def searchMatrix(self, matrix, target):

        numRows = len(matrix)
        numCols = len(matrix[0])

        i = 0

        # Point j to the first element in the last row
        j = numCols - 1

        # while i >= 0 and i <= numRows - 1 and j >= 0 and j <= numCols - 1:

        while 0 <= i <= numRows - 1 and 0 <= j <= numCols - 1:

            # Check if element is found.
            if matrix[i][j] == target:
                return True

            elif matrix[i][j] > target:
                j = j - 1
            else:
                i = i + 1

        return False


obj1 = Solution()
print(obj1.searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5))
print(obj1.searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20))
