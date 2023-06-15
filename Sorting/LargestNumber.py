def LargestNumber(nums):
    if len(nums)<1:
        return None
    maxVal = nums[0]
    for i in nums:
        maxVal = max(maxVal,i)

    return maxVal

print(LargestNumber([1,2,3,4,5,6,7,8,9]))
print(LargestNumber([1]))

def secondLargestnumber(nums):
    if len(nums)<=1:
        return None
    maxVal,secondMax = nums[0], nums[0]
    for i in nums:
        if i > maxVal:
            secondMax = maxVal
            maxVal = i
        if maxVal > i > secondMax:
            secondMax = i

    return secondMax

print(secondLargestnumber([1,2,3,4,5,6,7,8,9]))
print(secondLargestnumber([6, 8, 1, 2, 7]))
print(secondLargestnumber([1]))