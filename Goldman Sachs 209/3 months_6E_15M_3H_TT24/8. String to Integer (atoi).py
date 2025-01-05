class Solution:
    def myAtoi(self, s: str) -> int:
        # Whitespace: Ignore any leading whitespace (" ").
        s = s.lstrip()

        if len(s) is 0:
            return 0

        # Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
        sign = "-" if s[0] is "-" else "+" if s[0] is "+" else "++"

        # Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
        if not sign is "++":
            s = s[1:]

        # Conversion: 
        # Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
        
        s = s.lstrip("0")
        
        ls = None
        for i, d in enumerate(s):
            # d is not 0
            if d.isdigit():
                ls = i
            else:
                break
        if  ls is None:
            return 0

        # 2^32 -1 
        upper = 2147483647
        # -2^32
        lower = -2147483648
        
        return max(lower, min(upper, (-1 if sign is "-" else 1)*int(s[:ls+1])))
                    


# class Solution:
#     def myAtoi(self, s: str) -> int:
#         s = s.strip()
#         if not s: # if s: # s 被认为是 "真"，即它不是空的
#             return 0
#         signal=1
#         if s[0] == '-':
#             signal = -1
#             s=s[1:]
#         elif s[0]=='+':
#             s=s[1:]
        
#         re = 0
#         for ch in s:
#             if ch.isdigit():
#                 re=re*10+int(ch)
#             else:
#                 break

#         re=signal*re

#         MIN = (-2)**31
#         MAX = 2**31-1
#         if re<MIN:
#             return MIN
#         if re>MAX:
#             return MAX
#         return re

        
            

