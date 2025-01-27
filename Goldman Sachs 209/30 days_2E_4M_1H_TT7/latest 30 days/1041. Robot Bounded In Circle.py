class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # back to (0,0) & face north
        directions = [(0,1),(-1,0),(0,-1),(1,0)]
        start = [0,0]
        direction_idx = 0
        for i in instructions:
            if i == 'G':
                start[0]  += directions[direction_idx][0]
                start[1]  += directions[direction_idx][1]
            if i == 'L':
                direction_idx = (direction_idx+1)%4
                direction = directions[direction_idx]
            if i == 'R':
                direction_idx = (direction_idx-1)%4
                direction = directions[direction_idx]
        return start == [0,0] or direction_idx != 0
