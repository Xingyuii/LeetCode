class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction4 = [[0,1],[-1,0],[0,-1],[1,0]] # north, west, south, east
        x=0
        y=0
        i=0
        for move in instructions:
            if move == 'G':
                x+=direction4[i][0]
                y+=direction4[i][1] 
            if move == 'L':
                i = (i+1)%4
                direction = direction4[i]
    
            if move == 'R':
                i = (i-1)%4
                direction = direction4[i]
        
        return  (x==0 and y ==0) or i != 0 

