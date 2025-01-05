from typing import List
def trap(height: List[int]) -> int:
    n = len(height)
    l_max = [0] * n  # Array to store left max height
    r_max = [0] * n  # Array to store right max height
    area = 0

    l_max[0] = height[0]
    for i in range(1,n):
        # 1 to n-1
        l_max[i] = max(l_max[i-1],height[i])

    r_max[n-1] = height[n-1]
    for j in range(n-2,-1,-1):
        r_max[j] = max(r_max[j+1],height[j])
    
    for k in range(n):
        area += min(l_max[k],r_max[k])-height[k]
    return area
