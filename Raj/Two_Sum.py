class Solution(object):
    def twoSum(self, nums, target):
        j = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in j:
                return [j[complement], i]
            j[num] = i
        return []

i = [3, 2, 4]
j = 6
k = Solution()
print(k.twoSum(i, j))