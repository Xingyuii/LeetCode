# 文件名：Array/solution_001_two_sum.py

# 题目：两数之和
# LeetCode 题号：1
# 解题思路：使用哈希表来记录每个数的索引，查找目标值的补数
# 时间复杂度：O(n)
# 空间复杂度：O(n)

def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        if target - num in hashmap:
            return [hashmap[target - num], i]
        hashmap[num] = i

print(two_sum([1,2,3,5,6,7],11))