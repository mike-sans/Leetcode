class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            ret = int(str(x)[::-1])
        else:
            ret = int("-"+str(abs(x))[::-1])
        return ret if -2**31 <= ret <= 2**31 - 1 else 0
        