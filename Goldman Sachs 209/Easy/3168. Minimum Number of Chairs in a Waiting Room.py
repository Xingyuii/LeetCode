class Solution:
    def minimumChairs(self, s: str) -> int:
        seat=0
        min_seat =0
        for i in s:
            if i == 'E':
                seat+=1
                min_seat=max(min_seat,seat)
            else:
                seat-=1
        return min_seat

# Test cases
if __name__ == "__main__":
    solution = Solution()
# In Python, every script has a special built-in variable called __name__. 
# When you run a script directly, the value of __name__ is set to "__main__".

    # Example test cases
    print(solution.minimumChairs("EEELLL"))  # Output: 3
    print(solution.minimumChairs("ELEL"))    # Output: 1
    print(solution.minimumChairs("EEEELL"))  # Output: 4
    print(solution.minimumChairs("ELLE"))    # Output: 2

    # 写出来 开心 ^_^