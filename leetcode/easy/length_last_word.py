class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Time: O(n). Space: O(1)
        :type str: s
        :rtype int
        """
        # last = ""
        # for char in reversed(s):
        #     if char != " ":
        #         last += char
        #     elif last:
        #         break
        # return len(last)
        last_len = 0
        for c in reversed(s):
            if c != " ":
                last_len += 1
            elif last_len > 0:
                break
        return last_len


sol = Solution()
s = "H World"
expected = 5
print(sol.lengthOfLastWord(s))
print(len("World"))
