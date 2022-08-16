"""
Return the first negative number in each sub array of size k
If there is no negative number in a given sub array return 0
Output must be list
"""


def firstNegativeNumber(nums, k):
    finaArr = []
    negNum = []
    if len(nums) < k:
        return "Invalid"

    for i in range(len(nums)):
        if nums[i] < 0:  # Adding all the negative numbers to a list called negNum
            negNum.append(i)
        if i < k - 1:
            continue
        if len(negNum) == 0:  # If the length of negNum list is 0, appending 0 to finalArr
            finaArr.append(0)
        else:
            if negNum[0] < i - k + 1:  # If first number in negNum array is less than i-k+1
                # i.e., checking if the index is a part of window
                negNum.pop(0)  # If first number is not part of sliding window popping it from negNum list
            finaArr.append(nums[negNum[0]])  # Appending the least negative number in sliding window to finalArr
    return finaArr  # Returning finalArr


print(firstNegativeNumber([1, 2, -3, -4, -5, -6, 7, 8], 3) == [-3, -3, -3, -4, -5, -6])  # TestCase 1
print(firstNegativeNumber([1, 2, 4, 5, -6, 7, 8], 3) == [0, 0, -6, -6, -6])  # TestCase 2
print(firstNegativeNumber([-6, 7, 8], 3) == [-6])  # TestCase 3
print(firstNegativeNumber([-6, 7], 3) == "Invalid")  # TestCase 4
print(firstNegativeNumber([1, 2, -3, 4, 5, -6, 7, 8], 5) == [-3, -3, -3, -6])  # TestCase 5
print(firstNegativeNumber([-1, -2, -3, -4, -5, -6, -7, -8], 4) == [-1, -2, -3, -4, -5])  # TestCase 6
