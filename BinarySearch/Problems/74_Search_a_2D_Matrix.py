"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix.
This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        start = 0  # Initiating start pointer
        m = len(matrix)  # Calculating no.of rows
        n = len(matrix[0])  # Calculating no.of columns
        end = m * n - 1  # Calculating end-pointer
        while start <= end:
            mid = start + (end - start) // 2  # Calculating mid-pointer
            (x, y) = self.get2DIndex(mid, n)  # Calling method to get the 2d-Index position
            if matrix[x][y] == target:  # Returning true when the target is found
                return True
            elif matrix[x][y] < target:  # Updating start-pointer to the next value of mid-pointer
                # when the mid-value is less than target value
                start = mid + 1
            else:  # Updating end-pointer to the previous value of mid-pointer
                # when the mid-value is greater than target value
                end = mid - 1

        return False  # If the element is not found, returning false

    def get2DIndex(self, index, n):  # Method to calculate the 2d-Index values when 1D index value is provided.
        return index // n, index % n  # index // n returns the row value, % n returns the column value


obj1 = Solution()
assert obj1.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3) == True  # Test case 1
assert obj1.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) == False  # Test case 2
assert obj1.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 70) == False  # Test case 3
assert obj1.searchMatrix([[1, 3, 5], [10, 11, 16]], 1) == True  # Test case 4
assert obj1.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20]], 9) == False  # Test case 5
assert obj1.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20]], 7) == True  # Test case 6
assert obj1.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 23) == True  # Test case 7
