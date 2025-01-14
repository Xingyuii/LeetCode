class Solution:
    def findMin(self, nums: List[int]) -> int:
        Min = nums[0]
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                return nums[i]
        return Min
# O(n)

# what if using O(log(n))
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        n=len(nums)
        r=n-1
        while l<r:
            if nums[l]<nums[r]:
                r-=1
            else:
                l+=1
        return nums[l]



class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        n=len(nums)
        r=n-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        return nums[l]
