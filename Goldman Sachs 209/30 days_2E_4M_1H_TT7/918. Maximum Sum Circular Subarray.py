class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        def m(nums):
            current_sum = nums[0]
            max_sum = nums[0]
            for i in range(1,n):
                current_sum = max(current_sum +nums[i],nums[i])
                max_sum = max(current_sum,max_sum)
            return max_sum

        # 1. No cycle
        m1 = m(nums)
        # 2. linked cycle: total - min_sum
        m2 = m([-num for num in nums])
        if m1 < 0:
            return m1
        return max(m1,sum(nums)+m2)

#不看答案肯定想不到
class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Step 1: Calculate the non-circular maximum subarray sum (using sliding window)
        max_sum = float('-inf')
        current_sum = 0
        
        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        # Step 2: Calculate the total sum of the array
        total_sum = sum(nums)
        
        # Step 3: Calculate the minimum subarray sum (also using sliding window)
        min_sum = float('inf')
        current_min = 0
        
        for num in nums:
            current_min = min(num, current_min + num)
            min_sum = min(min_sum, current_min)

        # Step 4: If total_sum equals min_sum, it means all numbers are negative,
        # so we cannot form a circular subarray with a greater sum than the non-circular one
        if total_sum == min_sum:
            return max_sum
        
        # Step 5: The maximum sum for circular subarray is the total sum minus the minimum subarray sum
        circular_sum = total_sum - min_sum
        
        # Step 6: Return the maximum of non-circular and circular subarray sum
        return max(max_sum, circular_sum)

# 示例测试
solution = Solution()
print(solution.maxSubarraySumCircular([1, -2, 3, -2]))  # 输出: 3
print(solution.maxSubarraySumCircular([5, -3, 5]))      # 输出: 10
print(solution.maxSubarraySumCircular([-3, -2, -3]))    # 输出: -2
