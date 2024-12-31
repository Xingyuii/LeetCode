class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l = list(range(1,n+1))
        p = 0
        while len(l)>1:
            p = (p+k-1)%len(l) # -1 是减去删除点的index 1
            l.pop(p)
        return l[0]