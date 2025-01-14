class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:   
        def modify(ss):
            l = []
            for x in ss:
                if x == '#':
                    if l: 
                        l.pop()
                    else:
                        next
                else:
                    l.append(x)
                #print(l)
            return l
        return modify(s)==modify(t)
    
#OKKKK

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:   
        def modify(ss):
            l = []
            for x in ss:
                if x == '#':
                    if l: 
                        l.pop()
                else:
                    l.append(x)
                #print(l)
            return l
        return modify(s)==modify(t)