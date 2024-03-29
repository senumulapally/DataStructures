'''
Given an array of integers nums sorted in non-decreasing order, find the ending position of a given target value.
If target is not found in the array, return -1
You must write an algorithm with O(log n) runtime complexity.

Test Cases:
assert s1.getRightMostIndex([1,1,1], 1) == 0
assert s1.getRightMostIndex([1], 1) == 0
assert s1.getRightMostIndex([1, 2, 2, 3, 3, 3, 4], 3) == 3
assert s1.getRightMostIndex([1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5], 5) == 11
'''


def getLeftMostIndex(nums, target):
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
            end = mid - 1  # Moving the end-pointer to the previous value of mid-pointer as we are looking for
            # left most index.
        elif target < nums[mid]:
            end = mid - 1  # Updating end-pointer when target is less than the mid-pointer value
        else:
            start = mid + 1  # Updating start-pointer when target is greater than the mid-pointer value
    return index


assert getLeftMostIndex([1, 1, 1], 1) == 0  # Running Test Case 1
assert getLeftMostIndex([1], 1) == 0  # Running Test Case 2
assert getLeftMostIndex([1, 2, 2, 3, 3, 3, 4], 3) == 3  # Running Test Case 3
assert getLeftMostIndex([1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5], 5) == 11  # Running Test Case 4
assert getLeftMostIndex([1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5], 7) == -1  # Running Test Case 5
