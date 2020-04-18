#Time O(s) s - sum of all chars. Space O(1)
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                # If next string length == current string length,
                # So one of the strings is the longest substring for the rest.
                # If vertical match is false, is the index for taking the substring
                if len(strs[j]) == i or strs[j][i] != char:
                    return strs[0][:i]  # take substring
        return strs[0]

strs = ["flower","flow","flight"]

solution = Solution()
print(solution.longestCommonPrefix(strs))
