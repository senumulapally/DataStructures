"""
Find maximum (or minimum) sum of a subarray of size k
"""


def MaximumSubArray(k, nums):
    start, maxSum, windowSum = 0, 0, 0
    if k > len(nums):
        return "Invalid Range"
    for i in range(len(nums)):  # Looping through array
        windowSum += nums[i]  # Adding each element to the windowSum
        if i >= k - 1:  # When the loop reaches the K range
            maxSum = max(maxSum, windowSum)  # Finding max value between maxSum and WindowSum and
            # storing whichever is higher in maxSum variable
            windowSum -= nums[start]  # Subtracting starting element of previous window from windowSum
            start += 1  # Incrementing start pointer by 1 so that window moves by 1 element
    return maxSum  # Returning the max Sum.


print(MaximumSubArray(2, [100, 200, 300, 400]) == 700)
print(MaximumSubArray(4, [1, 4, 2, 10, 23, 3, 1, 0, 20]) == 39)
print(MaximumSubArray(3, [2, 3]) == "Invalid Range")
