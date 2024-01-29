class Solution:
    def isMatch(self, s: str, p: str):
        def findIt(ss: str, pp: str):
            tt = 0
            aapos = []
            c = 0
            while tt != -1:
                tt = ss.find(pp)
                if tt != -1:
                    aapos.append(tt+c)
                    ss = ss[:tt] + ss[tt+1:]
                    c += 1
                else:
                    break
            return aapos

        #go ahead and solve if there are no '*'
        if findIt(p,'*') == []:
            if len(p) == len(s):
                while len(p)>0:
                    if p[0] == '.' or p[0] == s[0]:
                        p = p[1:]
                        s = s[1:]
                    else: 
                        return False
                return True
            else:
                return False
        
        tempp = p
        ppos = []
        pa = []
        pb = []

        count1 = 0
        grow = ''

        # if constants surround start and end of p, then collapse them. update tempp and s
        while count1 < len(tempp):
            if count1 + 1 < len(tempp):
                if tempp[count1+1] == '*':
                    break

            if len(s) == 0:
                return False
            else:
                if tempp[count1] == '.' or tempp[count1] == s[count1]:
                    tempp = tempp[count1+1:]
                    s = s[count1+1:]
                else: 
                    return False

        count1 = len(tempp) - 1
        while count1 >= 0:
            if tempp[count1] == '*':
                break
            if len(s) == 0:
                return False
            else:
                if tempp[count1] == '.' or tempp[count1] == s[-1]:
                    tempp = tempp[:count1]
                    s = s[:-1]
                else:
                    return False

            count1 -= 1

        # making pa, pb, and ppos
        for i in range(len(tempp)):

            if tempp[i] == '*':
                grow = grow[:-1]

                pb.append(tempp[i-1])

                if len(grow) > 0:
                    pa.append(grow)

                ppos.append(len(pa)-1)
                grow = ''

            else:
                grow += tempp[i]
                # return [grow]

            if i == len(tempp) - 1 and len(grow) > 0:
                # if len(grow) > 0:
                pa.append(grow)

        success = False
        for i in range(len(s) - len(pa) + 1):

            tp = tempp[:-2] + (i * pb[-1])

            if pb[-1] != '.':
                if i > 0:
                    if i * pb[-1] != s[-i:]:
                        return False

            if self.isMatch(s,tp) == True:
                # success == True
                # break 
                return True


        return False