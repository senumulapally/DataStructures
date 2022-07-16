"""
Given an array of sorted numbers find the count of unique elements
"""


def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    startIndex = -1  # Initialising startIndex with -1
    endIndex = findIndex(nums, target, True)  # Finding the end index by calling findIndex method. Here 'True' is for
    # Right boundary index
    if endIndex != -1:  # If already endIndex is -1 no need to find the start index as the element is not found
        startIndex = findIndex(nums, target, False)  # Finding the end index by calling findIndex method.
        # Sending 'isRightIndex' as false as we are here finding left boundary index.
    return [startIndex, endIndex]  # Returning start and end indexes


def findIndex(nums, target, isRightIndex):
    """
    :type nums: List[int]
    :type target: int
    :type isRightIndex: bool
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
            if isRightIndex:  # checking if the requirement is for right index.
                start = mid + 1  # Moving the start-pointer to the next value of mid-pointer as we are looking for
            # right most index.
            else:
                end = mid - 1  # Moving the end-pointer to the previous value of mid-pointer as we are looking for
            # left most index.
        elif target < nums[mid]:
            end = mid - 1  # Updating end-pointer when target is less than the mid-pointer value
        else:
            start = mid + 1  # Updating start-pointer when target is greater than the mid-pointer value
    return index  # returning index


def getUniqueNumbersCount(nums, start, end):  # Recursive function to get unique numbers when
    # List of elements, start point and end point are provided
    """
    :type nums: List[int]
    :type start: int
    :type end: int
    :rtype: int
    """
    if start < 0 or start > len(nums)-1:  # Handled index out of bound exception for start pointer
        return 0
    if end < 0 or end > len(nums)-1:  # Handled index out of bound exception for end pointer
        return 0
    if start > end:  #
        return 0
    if start == end:  # Here, we have a unique value where start and end point to the same value so returning 1
        return 1

    mid = start + (end - start) // 2  # Calculating mid point
    [leftB, rightB] = searchRange(nums, nums[mid])  # Calculating range of mid-point
    count = 1  # Initialising count to 1 as mid-point is also a unique number.
    count += getUniqueNumbersCount(nums, start, leftB-1)  # Recursive call for right side array of mid-point
    count += getUniqueNumbersCount(nums, rightB+1, end)  # Recursive call for left side array of mid-point

    return count  # Returning count


def getCount(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return getUniqueNumbersCount(nums, 0, len(nums)-1)  # Returning the unique count


assert getCount([-2, -2, -1, 0, 1, 2, 2, 2, 3, 4, 4, 5, 5, 6, 6, 6, 7, 8]) == 11  # Testcase 1
assert getCount([-2, -2, -1, 0, 0, 1, 1, 2]) == 5  # Testcase 2
assert getCount([1, 1, 1]) == 1  # Testcase 3
