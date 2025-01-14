class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        n=len(time)
        matches=defaultdict(int)
        cnt=0
        for i in range(n):
            reminder = time[i]%60
            if ((60-reminder)%60) in matches:
                cnt+=matches[(60-reminder)%60]     
            matches[reminder] += 1
        return cnt