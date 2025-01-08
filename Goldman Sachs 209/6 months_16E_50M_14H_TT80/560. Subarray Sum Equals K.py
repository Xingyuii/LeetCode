#from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        sum_count = defaultdict(int)
        sum_count[0]=1
        for num in nums:
            prefix_sum += num
            # 当 prefix_sum - k 存在于 sum_count 中时，增加 count 的值
            if prefix_sum - k in sum_count:
                count += sum_count[prefix_sum - k]
            # 更新 prefix_sum 在 sum_count 中的频率    
            sum_count[prefix_sum] += 1
        return count

            
