"""
f(x) is a function. Its a increasing function. This means f(2)>f(1) and f(3)>f(2).
The value of f(x) can be negative. But since its a increasing function, at some value of x, f(x) will start becoming greater than zero.
Find the value of p for which f(p) is first positive number.
ie
f(p-1), f(p-2).... are all negative.
f(p) is positive
f(p+1), f(p+2).... are all positive
find the value of p

Example Test Case: f(x) = 2x-20. So until x =10, f(x) will be negative.
"""

class Solution(object):
    def firstPositiveNumber(self, formula):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        end = self.getPossibleIndex(formula)  # Calling method to get the possible index with positive value
        start = end // 2  # Initiating start-pointer to 2^i//2 i.e., 2^(i-1) as target is present before this index.
        while start <= end:
            mid = start + (end - start) // 2
            if self.functionReader(mid, formula) == "Positive" and self.functionReader(mid-1, formula) == "Negative":
                # If the mid-value is positive we cannot surely
                # say that it is the first positive value
                # Hence, checking the previous value,
                # If previous value is negative, returning mid-value.
                return mid
            elif self.functionReader(mid, formula) == "Negative":  # If, Mid-value is negative updating start-pointer
                # to next value of mid-pointer.
                start = mid + 1
            else:   # Else, updating end pointer to previous value of mid-pointer.
                end = mid - 1
        return -1

    def getPossibleIndex(self, formula):
        index = -1
        n = 0
        while index == -1:
            """
            divide the ranges like this. 
            2^0-2^1
            2^1-2^2
            2^2-2^3
            ....
            Do this until you get an invalid index or element greater than target. 
            your end will now point to 2^i. 
            start = (2^i)/2
            """
            val = self.functionReader(2**n, formula)
            if val == "Positive":
                index = 2 ** n
                return index
            n += 2
        return -1

    def functionReader(self, x, formula):
        val = eval(formula)  # Evaluating given formula for given value
        if val < 0:
            return "Negative"  # Returning positive if the function returns positive value
        else:
            return "Positive"  # Else returning negative


obj1 = Solution()
assert obj1.firstPositiveNumber("2*x-20") == 10  # Test Case 1
assert obj1.firstPositiveNumber("2*x-30") == 15  # Test Case 2
assert obj1.firstPositiveNumber("x-45") == 45  # Test Case 3
assert obj1.firstPositiveNumber("5*x-45") == 9  # Test Case 4