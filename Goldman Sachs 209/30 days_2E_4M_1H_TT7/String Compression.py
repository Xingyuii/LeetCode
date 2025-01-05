from typing import List
def compress(chars: List[str]) -> int:
    n = len(chars)
    write =0
    read =0
    while read < n:
        ch = chars[read]
        cnt=0
        while read <n and chars[read] == ch :
            read+=1
            cnt+=1
        
        #write ch
        chars[write] = ch
        write+=1
        #write cnt
        if cnt>1:
            for i in str(cnt):
                chars[write] = i
                write+=1
    print(chars)
    return write

chars = ["a", "a", "b", "b", "c", "c", "c"]
print(compress(chars))
