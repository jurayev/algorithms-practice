class Solution:
    def merge(self, nums1, m: int, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        Brute Force: Time: O(n+m). Space: O(1)
        """
        # nums1[m:] = nums2
        # nums1.sort()
        curr = 0
        for i in range(n):
            for j in range(curr, m+n):
                if nums1[j] > nums2[i]:
                    nums1[j], nums1[j+1:] = nums2[i], nums1[j:m+n-1]
                    break
                curr = j+1
            else:
                nums1[i + m] = nums2[i]
        return nums1


sol = Solution()
nums1 = [4,0,0,0,0,0]
m = 1
nums2 = [1,2,3,5,6]
n = 5
print(sol.merge(nums1, m, nums2, n))
