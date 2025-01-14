#思路正确，代码有点问题，先画图想清楚思路和边界条件
class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        # Calculate row cost
        if startPos[0] <= homePos[0]:
            rowCost = sum(rowCosts[startPos[0]+1:homePos[0]+1])
        else:
            rowCost = sum(rowCosts[homePos[0]:startPos[0]])
        
        # Calculate column cost
        if startPos[1] <= homePos[1]:
            colCost = sum(colCosts[startPos[1]+1:homePos[1]+1])
        else:
            colCost = sum(colCosts[homePos[1]:startPos[1]])
        
        # Total cost is row cost + column cost
        return rowCost + colCost
