#Time O(n) Space O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        previous = 0
        romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for c in reversed(s):
            if romans[c] < previous:
                result -= romans[c]
            else:
                result += romans[c]
            previous = romans[c]
        return result

s = "CXIX"
solution = Solution()
print(solution.romanToInt(s))