"""
Return the first negative number in each sub array of size k
If there is no negative number in a given sub array return 0
Output must be list
"""


def firstNegativeNumber(nums, k):
    windowArr = []
    finalArr = []
    if len(nums) < k:
        return "Invalid"
    for i in range(len(nums)):
        if i < k - 1:
            windowArr.append(nums[i])
            continue
        windowArr.append(nums[i])
        for j in range(k):
            if windowArr[j] < 0:
                finalArr.append(windowArr[j])
                break
            if j == k - 1:
                finalArr.append(0)
        windowArr.pop(0)
    return finalArr


print(firstNegativeNumber([1, 2, -3, 4, 5, -6, 7, 8], 3))  # TestCase 1
print(firstNegativeNumber([1, 2, 4, 5, -6, 7, 8], 3))  # TestCase 2
print(firstNegativeNumber([-6, 7, 8], 3))  # TestCase 3
print(firstNegativeNumber([-6, 7], 3))  # TestCase 4
print(firstNegativeNumber([1, 2, -3, 4, 5, -6, 7, 8], 5))  # TestCase 5
