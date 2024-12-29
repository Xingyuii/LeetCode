from typing import List
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    # 用一个字典（哈希表）来记录数组中的元素及其对应的索引。
    dic = {}
    
    # 遍历 nums，同时记录当前元素的值 num 和索引 i
    for i, num in enumerate(nums):
        # 检查当前元素 num 是否已经存在于字典中
        # 如果存在，并且当前索引与字典中记录的索引差值 <= k，则找到解，返回 True
        if num in dic and i - dic[num] <= k:
            return True
        
        # 更新字典，记录当前 num 的最新索引
        dic[num] = i
    
    # 如果遍历完都没有找到满足条件的元素对，返回 False
    return False

# test
nums = [1,2,3,1,2,3]
k=2
print(containsNearbyDuplicate(nums,k))