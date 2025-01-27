class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = defaultdict(int)

        for num in nums:
            frequent[num] += 1  # 直接累加，不需要判断是否存在

        # 按频率排序，取前 k 个
        sorted_items = sorted(frequent.keys(), key=lambda x: frequent[x], reverse=True)
        top_k = sorted_items[:k]  # 提取前 k 个数字

        return top_k
    
    # # 按频率排序，取前 k 个
    #     sorted_items = sorted(frequent.items(), key=lambda x: x[1], reverse=True)
    #     top_k = [item[0] for item in sorted_items[:k]]  # 提取前 k 个数字