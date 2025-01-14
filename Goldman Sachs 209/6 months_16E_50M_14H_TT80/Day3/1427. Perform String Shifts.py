class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        total_shift = 0
        for sh in shift:
            if sh[0]==0:
                total_shift-=sh[1]
            else:
                total_shift+=sh[1]
        total_shift=total_shift%len(s) ### 注意这里
        return s[-total_shift:]+s[:-total_shift]
