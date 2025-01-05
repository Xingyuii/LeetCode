class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s)==1:
            return s
        
        n=len(s)
        max_ls=s[0]
        max_length = 1

        # odd
        for i in range(n):
            l,r=i,i
            while l>=0 and r<n and s[l] == s[r]:
                if r-l+1>max_length:
                    max_ls = s[l:r+1]
                    max_length = r-l+1
                r+=1
                l-=1 
                     
        # even
        for i in range(n):
            l,r=i,i+1
            while l>=0 and r<n and s[l] == s[r]:
                if r-l+1>max_length:
                    max_ls = s[l:r+1]
                    max_length = r-l+1
                r+=1
                l-=1 
        return max_ls
