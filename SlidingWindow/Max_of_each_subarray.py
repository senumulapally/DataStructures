def maxOfSubArray(nums, k):
    low = 0
    high = 0
    n = len(nums)
    output = []
    maxNum = -1
    while high < n:
        if high - low + 1 < k:
            if nums[maxNum] < nums[high]:
                maxNum = high
            high += 1
            continue
            if nums[maxNum] < nums[high] and maxNum < low:
                maxNum = high

        output.append(nums[maxNum])

        low += 1
        high += 1
    return output
