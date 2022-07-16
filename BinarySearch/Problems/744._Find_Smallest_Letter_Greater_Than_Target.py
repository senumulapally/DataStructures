class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        start = 0  # Initiating start-pointer
        end = len(letters) - 1  # Initiating end-pointer

        if target < letters[end]:  # When the target letter is greater than the greatest letter in the list,
            # Index out of range error is occurred

            while start < end:  # Once the start>end the loop ends, we shall return the start-pointer
                # as it points to the next least element of the target
                mid = start + (end - start) // 2  # Calculating the mid-point.
                if letters[
                    mid] == target:  # If the mid-point value is equal to the target, next point value is returned
                    return letters[mid + 1]
                elif letters[mid] < target:  # When the mid-point letter is less than the given target,
                    # start-pointer is updated to the next point of mid-point
                    start = mid + 1
                else:  # Else, end-pointer is updated to the previous point of mid-point
                    end = mid - 1

            return letters[start]  # By the end of this loop, start pointer will be pointed to the next value
            # of the target. Hence, it is returned

        return "Range exceeded"  # This text is returned when the selected target's index is out of range.


obj1 = Solution()
assert obj1.nextGreatestLetter(["c", "f", "j"], "a") == "c"  # Test Case 1
assert obj1.nextGreatestLetter(["c", "f", "j"], "f") == "j"  # Test Case 2
assert obj1.nextGreatestLetter(["a", "b", "c", "f", "f"], "d") == "f"  # Test Case 3
assert obj1.nextGreatestLetter(["a", "b", "c", "f"], "g") == "Range exceeded"  # Test Case 4
assert obj1.nextGreatestLetter(["a", "b", "c", "f", "h"], "g") == "h"  # Test Case 5
assert obj1.nextGreatestLetter(["a", "b", "c", "c", "f", "h"], "g") == "h"  # Test Case 6
