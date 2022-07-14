"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of
 your product fails the quality check.
Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following
ones to be bad. You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a
function to find the first bad version. You should minimize the number of calls to the API.

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
"""


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1  # Initializing start-pointer
        end = n  # Initializing end-pointer
        position = 0  # Initializing position-pointer which gets the position of first bad version
        while start <= end:
            ''' 
            While loop ends when start-pointer is greater than end-pointer. 
            Loop condition is start<=end because when start = end either the target value 'found' or 'not found' 
            conditions are met 
            '''
            mid = start + (end - start) // 2  # Calculating mid-point (Integer Overflow exception handled)
            if isBadVersion(mid):  # If mid-position has bad version
                position = mid  # mid is assigned to Position
                end = mid - 1  # and end-pointer is set to mid-1
            else:
                start = mid + 1
                # if mid-pointer is not a bad version the start-pointer is set to mid+1 as the list before the mid
                # has all good versions and the next half of the list is to be searched for first bad version

        return position
