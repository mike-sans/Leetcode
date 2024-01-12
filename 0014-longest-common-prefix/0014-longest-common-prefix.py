class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        status = True
        for i in range(min([len(p) for p in strs])):
            temp = strs[0][i]
            for j in range(1,len(strs)):
                if temp != strs[j][i]:
                    status = False
                    break
            
            if status == False:
                break

            ans += temp

        return ans
