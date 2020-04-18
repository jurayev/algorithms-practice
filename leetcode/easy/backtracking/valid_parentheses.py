class Solution:
    # Time O(n) Space(n/2)
    def isValid(self, s: str) -> bool:
        if s == "":  # if empty string, valid
            return True
        if len(s) % 2 == 1:  # if uneven, not valid
            return False
        brackets = {"(": ")", "{": "}", "[": "]"}
        trace = []
        for c in s:
            if c in brackets.keys():
                trace.append(brackets[c])
            elif trace and trace.pop() == c:  # # if trace is empty == False
                continue
            else:
                return False
        return not trace  # if trace is empty -> True, else ->False

solution = Solution()
s = "{({[]})[]}{}"
print(solution.isValid(s))
