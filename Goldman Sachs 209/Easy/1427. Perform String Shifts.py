from typing import List
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        sh = 0
        for i in shift:
            if i[0]==0:
                sh = sh-i[1]
                #print(i[1])
            else:
                sh = sh+i[1]
                #print(i[1])
        sh %= len(s) # Ensure sh is within the bounds of the string length
        # k = sum((2*x-1)*y for x,y in shift)%len(s)
        return s[-sh:] + s[:-sh] 
    
# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.stringShift("abcdef", [[1, 2], [0, 4]]))  # Output: "cdefab"
    print(solution.stringShift("abcdef", [[0, 6]]))          # Output: "abcdef"
    print(solution.stringShift("abcdef", [[1, 8]]))          # Output: "efabcd"
    print(solution.stringShift("abcdef", [[1, 100]]))        # Output: "efabcd"

