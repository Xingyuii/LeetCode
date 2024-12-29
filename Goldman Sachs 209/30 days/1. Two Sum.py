# 这题非常简单，但是需要深刻理解字典的作用
from typing import List
# My stupid solution
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             if target - nums[i] in nums and i != nums.index(target - nums[i]):
#                 return [i,nums.index(target - nums[i])]


#Best solution in leetcode
def twoSum(nums: List[int], target: int) -> List[int]:
    numMap = {}

    for i in range(len(nums)):
        if nums[i] in numMap:
            return [i, numMap[nums[i]]]
        else:
            numMap[target - nums[i]] = i


# test
nums=[1,2,7,5,9]
target = 9
print(twoSum(nums,target))