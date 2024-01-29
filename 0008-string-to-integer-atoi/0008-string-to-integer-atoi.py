class Solution:
    def myAtoi(self, s: str) -> int:

        if s == "":
            return 0
        
        neg = True
        i = 0
        l = len(s)
        r = ""
        o = 0

        while i < l:
            if s[i] == " ":
                i = i + 1
            elif s[i] == '-':
                neg = True
                i = i + 1
                break
            elif s[i] == '+':
                neg = False
                i = i + 1
                break
            else:
                neg = False
                break

        while i < l:
            if s[i].isdigit():
                o = o * 10 + int(s[i])
                i = i + 1
            else:
                break

        if neg == True:
            o = -o

        if o >= 2**31:
            o = (2**31)-1
        elif o < -(2**31):
            o = -(2**31)

        return o