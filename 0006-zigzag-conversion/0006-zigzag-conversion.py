class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        out = ""

        if numRows == 1:
            return s
        
        arr = [[] for x in range(numRows)]

        skipnum = numRows*2-2

        i = 0
        while i < len(s):
            if i % skipnum <= (skipnum / 2):
                t = i % skipnum
            else:
                t = -((i % skipnum) - skipnum)
            
            arr[t].append(i)
            
            i = i + 1
        
        flat_indices = [q for sublist in arr for q in sublist]

        out = ''.join(s[b] for b in flat_indices)
        return out
            