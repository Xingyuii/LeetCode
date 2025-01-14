from typing import List

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        # 定义转换函数
        def mapped_value(num: int) -> int:
            new_num = 0
            for digit in str(num):
                new_num = new_num * 10 + mapping[int(digit)]  # 使用映射值构造新数字
            return new_num

        # 使用 sorted，按映射值排序
        return sorted(nums, key=mapped_value)
