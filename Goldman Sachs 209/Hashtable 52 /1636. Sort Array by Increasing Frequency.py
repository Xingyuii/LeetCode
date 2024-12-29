from typing import List
def frequencySort(nums: List[int]) -> List[int]:
    dic={}
    for i in nums:
        dic[i] = dic.get(i,0)+1
    nums.sort(key=lambda x: (dic[x],-x))
    return nums

nums=[-9,-9,-8,-8,9,9,8,8,1,2,4]
print(frequencySort(nums))