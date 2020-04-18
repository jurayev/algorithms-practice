class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        :type haystack: str
        :type needle: str
        :rtype int
        Complexity - Time: O(n-m+1), Space: O(1). Where n=len(haystack), m = len(needle)
        """
        if not needle or haystack == needle:
            return 0
        len_h = len(haystack)
        len_n = len(needle)
        for i in range(len_h - len_n + 1):
            # if (len(haystack) - i) < len(needle):
            #     return -1
            if haystack[i] == needle[0]:
                if haystack[i:i+len_n] == needle:
                    return i
                # for j in range(1, len(needle)):
                #     if haystack[i+j] != needle[j]:
                #         break
                # else:
                #     return i
        return -1

haystack = "mississippi"
needle = "issipi"

sol = Solution()
res = sol.strStr(haystack, needle)
print(res)
