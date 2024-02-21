# Description:
# Given two integers `left` and `right` representing the range `[left, right]`, return the bitwise AND of all numbers in this range, inclusive.

# Approach:
#To find the bitwise AND of numbers in the given range, we identify the common prefix of the binary representations of `left` and `right`. The common prefix represents the bits that are the same for all numbers in the range. We perform right shifts on both `left` and `right` until they are equal. The number of shifts performed indicates the length of the common prefix. Finally, we left-shift one of the numbers by the same number of positions and return the result.

# Time Complexity:
# The time complexity of this approach is O(log n), where n is the range between `left` and `right`.

# Space Complexity:
# The space complexity is O(1) as we use only a constant amount of additional space.

# Python Solution:

# ```python
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shifts = 0
        while left < right:
            left >>= 1
            right >>= 1
            shifts += 1
        return left << shifts
# ```

# ```python
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right > left:
            right &= (right - 1)  # Clear the least significant bit
        return right
# ```
