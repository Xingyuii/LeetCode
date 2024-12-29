class Solution:
    def romanToInt(self, s: str) -> int:
        smap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        cnt=0
        n=len(s)
        for i in range(n-1):
            # 如果当前字符比前一个字符的值小，则加上它；否则，减去它。
            if smap[s[i]]<smap[s[i+1]]:
                cnt -= smap[s[i]]
            else:
                cnt+=smap[s[i]]
        cnt+=smap[s[-1]]
        return cnt
        