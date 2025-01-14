class Solution:
    def betterCompression(self, compressed: str) -> str:
        #construct a hashmap
        better_map={}
        n=len(compressed)
        i=0
        re=[]
        while i < n:
            char = compressed[i]
            cnt = 0
            i+=1
            while i<n and compressed[i].isdigit():
                cnt=cnt*10+int(compressed[i])
                i+=1
            if char in better_map:
                better_map[char]=better_map[char]+cnt
            else:
                better_map[char]=cnt
        for char in sorted(better_map):
            re.append(f"{char}{better_map[char]}")
        #print(re)
        return ''.join(re)

# defaultdic is a better method


        