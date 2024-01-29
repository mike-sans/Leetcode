# Non-string solution

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        array = []
        p = x
        while p != 0:
            t = p % 10
            array.append(t)
            p = (p-t)/10

        for h in range(len(array)//2 + 1):
            if (array[h] != array[len(array)-1-h]):
                return False

        return True
        