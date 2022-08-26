def printfirstNumber(nums, k):
    low = 0
    high = 0
    output = []
    n = len(nums)
    while high < n:
        if high-low+1 < k:
            high = high + 1
            continue

        output.append(nums[low])

        low = low + 1
        high = high + 1

    return output

def printLastNumber(nums, k):
    low = 0
    high = 0
    output = []
    n = len(nums)
    while high < n:
        if high-low+1 < k:
            high = high + 1
            continue

        output.append(nums[high])

        low = low + 1
        high = high + 1

    return output
print(printfirstNumber([1,2,3,4,5,6], 2))
print(printfirstNumber([1,2,3,4,5,6], 3))

print(printLastNumber([1,2,3,4,5,6], 2))
print(printLastNumber([1,2,3,4,5,6], 3))
