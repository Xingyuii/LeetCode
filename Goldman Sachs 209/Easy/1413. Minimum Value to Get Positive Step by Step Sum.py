from typing import List
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # startValue + minSum > 1 -> find min Presum
        # startValue>=1
        preSum = 0
        minSum = 0

        for num in nums:
            preSum += num
            minSum = min(preSum,minSum)
        return 1-minSum if minSum<0 else 1

if __name__ == "__main__":
    solution = Solution()
    print(solution.minStartValue(nums =[-3,2,-3,4,2]))


