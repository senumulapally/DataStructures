'''
Given an array of integers nums sorted in non-decreasing order, find the ending position of a given target value.
If target is not found in the array, return -1
You must write an algorithm with O(log n) runtime complexity.

Test Cases:
assert s1.getRightMostIndex([1,1,1], 1) == 2
assert s1.getRightMostIndex([1], 1) == 0
assert s1.getRightMostIndex([1, 2, 2, 3, 3, 3, 4], 3) == 5
assert s1.getRightMostIndex([1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5], 4) == 10
'''


def getRightMostIndex(nums, target):
    """
            :type nums: List[int]
            :type target: int
            :rtype: int
    """
    start = 0 # Initializing start-pointer
    end = len(nums) - 1  # Initializing end-pointer
    while start <= end:
        ''' 
        While loop ends when start-pointer is greater than end-pointer. 
        Loop condition is start<=end because when start = end either the target value 'found' or 'not found' conditions 
        are met 
        '''
        mid = start + (end - start) // 2  # Calculating mid-point (Integer Overflow exception handled)
        if target < nums[mid]:
            end = mid - 1  # Updating end-pointer when target is less than the mid-pointer value
        elif target > nums[mid]:
            start = mid + 1  # Updating start-pointer when target is greater than the mid-pointer value
        else:
            break  # Breaking the loop when the target value matched mid-pointer value

    while mid < len(nums)-1:  # Looping while mid-value is less than length of array
        if target == nums[mid + 1]:  # Condition to find if the next value is still the target value
            mid += 1  # If yes, mid-pointer is moved to the next value
        else:
            break  # Else if there is some other value than the target value, the loop is broken
    return mid  # Mid-value, pointed to the right most index of target value is returned.


print(getRightMostIndex([1, 1, 1], 1))  # Running Test Case 1
print(getRightMostIndex([1], 1))  # Running Test Case 2
print(getRightMostIndex([1, 2, 2, 3, 3, 3, 4], 3))  # Running Test Case 3
print(getRightMostIndex([1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5], 4))  # Running Test Case 4

