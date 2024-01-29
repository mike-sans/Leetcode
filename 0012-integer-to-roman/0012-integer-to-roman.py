class Solution:
    def intToRoman(self, num: int) -> str:
        val3 = num//1000
        num = num - 1000*val3
        val2 = num//100
        num = num - 100*val2
        val1 = num//10
        num = num - 10*val1
        val0 = num
        
        out = ""
        for i in range(val3):
            out = out + "M"

        if val2>=5:
            if val2 == 9:
                out = out+ "CM"
            else:
                out = out+"D"
                for i in range(val2-5):
                    out = out + "C"
        else:
            if val2 == 4:
                out = out + "CD"
            else:
                for i in range(val2):
                    out = out + "C"
        
        if val1>=5:
            if val1 == 9:
                out = out+ "XC"
            else:
                out = out+"L"
                for i in range(val1-5):
                    out = out + "X"
        else:
            if val1 == 4:
                out = out + "XL"
            else:
                for i in range(val1):
                    out = out + "X"
        
        if val0>=5:
            if val0 == 9:
                out = out+ "IX"
            else:
                out = out+"V"
                for i in range(val0-5):
                    out = out + "I"
        else:
            if val0 == 4:
                out = out + "IV"
            else:
                for i in range(val0):
                    out = out + "I"

        return out

        alist = [mval, dval, cval, lval, xval, vval, ival]
        blist = ["M", "D", "C", "L", "X", "V", "I"]
        for i in range(len(alist)):
            for j in range(alist[i]):
                out = out + blist[i]
        
        return out


        mval = num//1000
        num = num-1000*mval
        dval = num//500
        num = num - 500*dval
        cval = num//100
        num = num - 100*cval
        lval = num//50
        num = num - 50*lval
        xval = num//10
        num = num - 10*xval
        vval = num //5
        num = num - 5*vval
        ival = num