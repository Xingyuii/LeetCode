class Solution:
    def isPalindrome(self, s: str) -> bool:
        sl = s.lower()
        sn=""
        for x in sl:
            #if 'a' <= x <= 'z' or x.isdigit():
            if x.isalnum():
                sn+=x
        return sn==sn[::-1] 
