class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        start = 0  # Initiating start-pointer
        end = len(letters) - 1  # Initiating end-pointer

        while start <= end:  # Once the start>end the loop ends, we shall return the start-pointer
            # as it points to the next least element of the target
            mid = start + (end - start) // 2  # Calculating the mid-point.
            if letters[mid] <= target:  # When the mid-point letter is less than or equal to the given target,
                # start-pointer is updated to the next point of mid-point
                start = mid + 1
            else:  # Else, end-pointer is updated to the previous point of mid-point
                end = mid - 1

        return letters[start % len(letters)]  # By the end of this loop, start pointer will be pointed to the next value
        # of the target. Hence, it is returned
        # When the index is out of range, start % length of numbers will return
        # the reminder as 0 as start will be pointed to one value greater than the last index value.
        # Hence, first letter in the array will be returned.


obj1 = Solution()
assert obj1.nextGreatestLetter(["c", "f", "j"], "a") == "c"  # Test Case 1
assert obj1.nextGreatestLetter(["c", "f", "j"], "f") == "j"  # Test Case 2
assert obj1.nextGreatestLetter(["a", "b", "c", "f", "f"], "d") == "f"  # Test Case 3
assert obj1.nextGreatestLetter(["a", "b", "c", "f"], "g") == "a"  # Test Case 4
assert obj1.nextGreatestLetter(["a", "b", "c", "f", "h"], "g") == "h"  # Test Case 5
assert obj1.nextGreatestLetter(["a", "b", "c", "c", "f", "h"], "g") == "h"  # Test Case 6
assert obj1.nextGreatestLetter(["e", "e", "e", "e", "e", "e", "n", "n", "n", "n"], "e") == "n"  # Test Case 7
assert obj1.nextGreatestLetter(["e", "e", "e", "e", "e", "e", "n", "n", "n", "n"], "f") == "n"  # Test Case 8
