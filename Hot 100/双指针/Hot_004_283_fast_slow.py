#给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#请注意 ，必须在不复制数组的情况下原地对数组进行操作。

def moveZeroes(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        #快慢双指针 slow维护非0数组
        slow=fast=0
        while fast<len(nums):
            if nums[fast] !=0:
                nums[slow], nums[fast] = nums[fast],nums[slow]
                slow+=1
            fast+=1
        #return nums

nums = [0,1,0,3,12]
#print(moveZeroes(nums)) Wrong cuz moveZeroes doesn`t have a return
moveZeroes(nums)
print(nums) # must save before run