class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        for num in nums:
            if gas < 0: return False
            if num > gas: 
                gas = num
            gas -= 1 #每下一步i+1,消耗一个gas
        return True
