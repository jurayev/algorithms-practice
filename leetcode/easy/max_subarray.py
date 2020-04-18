class Solution:
    def maxSubArray(self, nums):
        summ = nums[0]
        maxx = nums[0]
        for i in range(1, len(nums)):
            if summ < 0:
                summ = nums[i]
            else:
                summ += nums[i]
            if maxx < summ:
                maxx = summ
        return maxx

nums = [-2,1,-3,4,-1,2,1,-5,4]
expected = 6