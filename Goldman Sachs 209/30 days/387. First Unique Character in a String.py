from typing import List
def firstUniqChar(s: str) -> int:
    for i in range(len(s)):
        if s[i] not in (s[0:i] + s[i+1:]):
            return i
    return -1

str = 'leetcode'
print(firstUniqChar(str))

# This is a simple question so there are many possible solutions

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         for i in range(len(s)):
#             if s.find(s[i]) == s.rfind(s[i]):
#                 return i
#         return -1

#also we can use s.count[s[i]]