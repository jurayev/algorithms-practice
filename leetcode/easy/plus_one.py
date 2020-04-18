class Solution:
    def plusOne(self, digits):
        """
        if non-9, add up one
        if 9, change to 0
        if all 9ns, add one element at the begining

        Time complexity O(n) and Space: O(1)
        :type digits: List[int]
        :rtype List[int]
        """
        for i in reversed(range(len(digits))):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        digits.insert(0, 1)
        return digits

sol = Solution()
digits = [1,9,9,9]
print(sol.plusOne(digits))
