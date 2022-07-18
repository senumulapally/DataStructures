"""
Given an integer array nums sorted in non-decreasing order and an integer target, return true if target
is a majority element, or false otherwise. A majority element in an array nums is an element
that appears more than nums.length / 2 times in the array.
"""


class Solution(object):
    def isMajorityElement(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        start = 0
        end = len(nums)-1
        mid = start + (end - start)//2
        if nums[mid] != target:
            return False

        [startIndex, endIndex] = self.searchRange(nums, target)  # Calculating range of target element
        elementLength = (endIndex - startIndex) + 1  # Finding the element length in array
        if elementLength > len(nums) / 2 and startIndex >= 0 and endIndex >= 0:  # If element length is greater than
            # ListLength/2 then it is a majority element
            return True  # Hence, returning true
        else:
            return False  # Else, false

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        startIndex = -1
        endIndex = self.findIndex(nums, target, True)
        if endIndex != -1:
            startIndex = self.findIndex(nums, target, False)
        return [startIndex, endIndex]

    def findIndex(self, nums, target, isRightIndex):
        """
                    :type nums: List[int]
                    :type target: int
                    :rtype: int
            """
        start = 0  # Initializing start-pointer
        end = len(nums) - 1  # Initializing end-pointer
        index = -1  # Initializing flag parameter with zero
        while start <= end:
            ''' 
            While loop ends when start-pointer is greater than end-pointer. 
            Loop condition is start<=end because when start = end either the target value 'found' or 'not found' conditions 
            are met 
            '''
            mid = start + (end - start) // 2  # Calculating mid-point (Integer Overflow exception handled)
            if target == nums[mid]:
                index = mid  # Updating flag with the latest index of target value
                if isRightIndex:
                    start = mid + 1  # Moving the start-pointer to the next value of mid-pointer as we are looking for
                # right most index.
                else:
                    end = mid - 1  # Moving the end-pointer to the previous value of mid-pointer as we are looking for
                # left most index.
            elif target < nums[mid]:
                end = mid - 1  # Updating end-pointer when target is less than the mid-pointer value
            else:
                start = mid + 1  # Updating start-pointer when target is greater than the mid-pointer value
        return index


obj1 = Solution()
assert obj1.isMajorityElement([2, 4, 5, 5, 5, 5, 5, 6, 6], 5) == True  # Test Case 1
assert obj1.isMajorityElement([438885258], 786460391) == False  # Test Case 2
assert obj1.isMajorityElement([2, 4, 5, 5, 5, 5, 5, 6, 6], 6) == False  # Test Case 3
assert obj1.isMajorityElement([2, 4, 5, 5, 5, 5, 5, 6, 6], 2) == False  # Test Case 4
assert obj1.isMajorityElement([2, 4, 5, 5, 5, 5, 5, 6, 6], 1) == False  # Test Case 5
