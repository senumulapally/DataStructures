from collections import deque


def firstNegativeNumber(nums , k):
    if len(nums) < k:
        return "Invalid"
    low = 0
    high = 0
    output = []
    queue = deque()
    n = len(nums)
    while high < n:
        if nums[high] < 0:
            queue.append(high)
        if high-low+1 < k:
            high += 1
            continue
        if len(queue) <= 0:
            output.append(0)
        else:
            if queue[0] < high - k + 1:
                queue.popleft()
            output.append(nums[queue[0]])
        low = low + 1
        high = high + 1

    return output


print(firstNegativeNumber([1, 2, -3, -4, -5, -6, 7, 8], 3) == [-3, -3, -3, -4, -5, -6])  # TestCase 1
print(firstNegativeNumber([1, 2, 4, 5, -6, 7, 8], 3) == [0, 0, -6, -6, -6])  # TestCase 2
print(firstNegativeNumber([-6, 7, 8], 3) == [-6])  # TestCase 3
print(firstNegativeNumber([-6, 7], 3) == "Invalid")  # TestCase 4
print(firstNegativeNumber([1, 2, -3, 4, 5, -6, 7, 8], 5) == [-3, -3, -3, -6])  # TestCase 5
print(firstNegativeNumber([-1, -2, -3, -4, -5, -6, -7, -8], 4) == [-1, -2, -3, -4, -5])  # TestCase 6
