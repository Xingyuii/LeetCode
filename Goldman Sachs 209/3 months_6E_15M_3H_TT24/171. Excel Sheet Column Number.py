def titleToNumber(columnTitle: str) -> int:
    ch ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dic = {}
    v=1
    for c in ch:
        dic[c]=v
        v+=1
    re = 0
    # 遍历 columnTitle，按位计算
    for s in columnTitle:
        re = re * 26 + dic[s]  # 每一位字符映射到对应的数字并加权
    return re

#test
columnTitle="AB"
print(titleToNumber(columnTitle))

# # 1. for & enumerate

# - 时间复杂度：for 和 enumerate 都是 O(n)，没有差别。
# - 空间复杂度：两者都是 O(1)，enumerate 会稍微消耗更多的内存，但差异微乎其微。
# - 使用场景：
    
#     如果只需要值：使用普通的 for 循环。
#     如果需要索引值：使用 enumerate。
#     for index, item in enumerate(iterable):
#         print(index, item)

# # 2. ord() 是一个Python内置函数，用来返回给定字符对应的 Unicode（或ASCII）码点（code point)
# def titleToNumber(columnTitle: str) -> int:
#     re=0
#     for s in columnTitle:
#         re = re*26 + ord(s)-ord("A")+1
#     return re
