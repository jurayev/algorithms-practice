class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype int
        Brute force TC: O(n)
        Binary Search TC: O(log n)
        """
        # for i in range(len(nums)):
        #     if target <= nums[i]:
        #         return i
        # return len(nums)

        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

            # if high == low:
            #     if target <= nums[low]:
            #         return low
            #     else:
            #         return low + 1

        return low

nums = [1,3,5,6]
target = 2
sol = Solution()
res = sol.searchInsert(nums, target)
print(res)
