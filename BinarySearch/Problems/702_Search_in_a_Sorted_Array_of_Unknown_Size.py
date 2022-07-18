"""
 You have a sorted array of unique elements and an unknown size. You do not have an access to the array but
 you can use the ArrayReader interface to access it. You can call ArrayReader.get(i) that:
 returns the value at the ith index (0-indexed) of the secret array (i.e., secret[i]), or
 returns 231 - 1 if the i is out of the boundary of the array.
 You are also given an integer target.
 Return the index k of the hidden array where secret[k] == target or return -1 otherwise.
 You must write an algorithm with O(log n) runtime complexity.
 This is ArrayReader's API interface.
 You should not implement it, or speculate about its implementation
"""
# class ArrayReader(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """

class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        end = self.getPossibleIndex(reader, target)  # Calling method to get the possible index or possible smallest
        # invalid index and assigning it to the end-pointer.
        start = end//2  # Initiating start-pointer to 2^i//2 i.e., 2^(i-1) as target is present before this index.
        while start <= end:
            mid = start + (end - start) // 2
            if self.ArrayReader(reader, mid) == target:
                return mid
            elif self.ArrayReader(reader, mid) < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1

    def getPossibleIndex(self, reader, target):
        index = -1
        n = 0
        while index == -1:
            """
            divide the ranges like this. 
            2^0-2^1
            2^1-2^2
            2^2-2^3
            ....
            Do this until you get an invalid index or element greater than target. 
            your end will now point to 2^i. 
            start = (2^i)/2
            """
            val = self.ArrayReader(reader, 2**n)
            if val >= target:
                index = 2 ** n
                return index
            n += 2
        return -1

    def ArrayReader(self, reader, index):
        if index > len(reader)-1:
            return 2**31 - 1
        else:
            return reader[index]

obj1 = Solution()
print(obj1.search([-1, 0, 3, 5, 9, 12], 9))  # Test case 1
print(obj1.search([-1, 0, 3, 5, 9, 12], 13))  # Test case 2
print(obj1.search([-1, 0, 3, 5, 9, 12], -3))  # Test case 3
print(obj1.search([-1, 0, 3, 5, 9, 12], 5))  # Test case 4
print(obj1.search([5], 5))  # Test case 5