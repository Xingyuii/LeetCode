class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2 #避免整数溢出
            # Check if mid is a peak element
            if mid > 0 and nums[mid - 1] > nums[mid]:
                right = mid - 1
            # If the right neighbor is greater, move to the right half
            elif mid < len(nums) - 1 and nums[mid + 1] > nums[mid]:
                left = mid + 1
            else:
                return mid