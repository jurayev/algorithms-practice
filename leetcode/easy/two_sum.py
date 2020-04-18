# time complexity O(n^2). space complexity O(1) runtime~5932ms
def twoSum(nums, target):
    for i in range(len(nums) - 1):
       for j in range(i+1, len(nums)):
            if target - nums[i] == nums[j]:
                return [i, j]

# time complexity O(n). space complexity O(n) runtime~52ms
def twoSumTwoPassHMap(nums, target):
   hmap = {nums[i]: i for i in range(len(nums))}
   for j in range(len(nums)):
       complement = target - nums[j]
       if complement in hmap.keys() and hmap[complement] != j:
           return [j, hmap[complement]]

# time complexity O(n). space complexity O(n) runtime~44ms
def twoSumOnePassHMap(nums, target):
    hmap = {}
    for j in range(len(nums)):
        complement = target - nums[j]
        if complement in hmap.keys():
            return [hmap[complement], j]
        hmap[nums[j]] = j

nums = [3, 2, 4, 15]
target = 6
result = twoSum(nums, target)
print(result)
