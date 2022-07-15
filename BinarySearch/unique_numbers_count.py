"""
Given an array of sorted numbers find the count of unique elements
"""


def getUniqueNumbersCount(nums):
    arrLen = len(nums)  # Calculating length of list
    flag = None  # Assigning None to the flag
    count = 0  # Initialising number os elements in list to Zero
    for index in range(0, arrLen):  # Looping through the list
        if flag != nums[index]:  # Whenever a new number is found this condition will become true
            flag = nums[index]  # The flag will be updated to the new number
            count += 1  # and count will be increased by 1
    return count  # Returning count of unique values.


print(getUniqueNumbersCount([-2, -2, -1, 0, 1, 2, 2, 2, 3, 4, 4, 5, 5, 6, 6, 6, 7, 8, 9]))
