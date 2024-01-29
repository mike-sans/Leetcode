# Slow solution but it's my own and it works, I didn't think of the smart (comparing left to right index and moving the smaller one inward) method.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = max(height)
        found = [[0,len(height)-1] for i in range(l+1)]

        i = min(height[0], height[-1])
        fail = False
        while i <= l:
            if i != 0:
                found[i] = []
                for j in range(found[i-1][0], len(height)):
                    if height[j] >= i:
                        found[i].append(j)
                        break
                    if j == len(height)-1:
                        fail = True
                        break
                for j in range(len(height)-1, -1, -1):
                    if height[j] >= i:
                        found[i].append(j)
                        break
                    if j == 0:
                        fail = True
                        break

            if fail == True:
                break

            if found[i][0] >= found[i][1]:
                break         
            
            i += 1

        found = [found[member] for member in range(len(found)) if member < i]

        maxval = 0
        for t in range(len(found)):
            if t*(found[t][1]-found[t][0]) > maxval:
                maxval = t*(found[t][1]-found[t][0])
        
        return maxval