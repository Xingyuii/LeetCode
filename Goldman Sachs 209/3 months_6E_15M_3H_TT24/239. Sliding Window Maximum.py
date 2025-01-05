# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         MAX = [] 
#         for r in range(k-1,len(nums)):
#             l = r-k+1
#             MAX.append(max(nums[l:r+1]))
#         return MAX
    
# TimeError


from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 存储结果
        MAX = []
        # 双端队列，存储元素的索引
        dq = deque()
        
        for i in range(len(nums)):
            # 移除队列中超出窗口范围的索引
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # 移除队列中所有比当前元素小的索引
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            # 将当前元素的索引加入队列
            dq.append(i)
            
            # 当窗口大小达到 k 时，加入结果
            if i >= k - 1:
                MAX.append(nums[dq[0]])
        
        return MAX

#太难想了。。