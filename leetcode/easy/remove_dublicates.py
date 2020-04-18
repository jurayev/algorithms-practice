class Solution:
    #TC: O(n), SC: O(1)
    def remove_duplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        j = 0

        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]

        return j + 1

nums = [0,0,1,1,1,2,2,3,3,4]

sol = Solution()
ind = sol.remove_duplicates(nums)
print(nums[:ind])
