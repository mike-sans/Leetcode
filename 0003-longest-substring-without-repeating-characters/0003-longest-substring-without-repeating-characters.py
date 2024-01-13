class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        if len(set(s)) == len(s):
            return len(s)
        count = 1
        end = False
        while True:
            success = False
            for i in range(len(s)-count):

                if len(s[i:i+count+1]) == len(set(s[i:i+count+1])):
                    success = True
                    count += 1
                    break

            if success == False:
                break
        return(count)