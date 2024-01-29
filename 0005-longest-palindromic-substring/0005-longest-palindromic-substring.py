class Solution:
    def longestPalindrome(self, s: str) -> str:
        def cycle(p: str, c: int, parray, ti) -> [str, bool, list]:
            success = False
            k = ""
            yik = []

            if new == 0:
                for y in range(len(p) - c):
                    if y in parray:
                        k = p[y : y + c + 1]

                        if k == k[::-1]:
                            yik.append(y)
            if new == 1:
                for y in parray:
                    if p[y] == p[y + c]:
                        yik.append(y)

            if len(yik)>0:
                bell = yik[-1]
                return p[bell:bell+c+1], True, yik
            else:
                return "fail", False, yik

        templast = []
        count = 0
        strike = 0
        new = 0

        array = [i for i in range(len(s))]

        while count < len(s):
            tempans = cycle(s, count, array, new)
            array = tempans[2]

            if tempans[1] == True:
                templast = tempans[0]
                new = 1
                if count + 2 < len(s):
                    # shift the list
                    array = [x - 1 for x in array]
                    array = [x for x in array if not (x < 0 or x + count + 2 >= len(s))]
                    count = count + 2

                elif count + 1 < len(s):
                    new = 0
                    for i in range(len(s)):
                        array.append(i)
                    array = [x for x in array if not (x < 0 or x + count + 1 >= len(s))]
                    tempans = cycle(s, count + 1, array, new)
                    if tempans[1] == True:
                        templast = tempans[0]
                        break
                    else:
                        break
                else:
                    break

            if tempans[1] == False:
                new = 0
                if strike == 0:
                    strike = 1
                    count = count - 1
                    # reset list to all
                    array = []
                    for i in range(len(s)):
                        array.append(i)
                    array = [x for x in array if not (x < 0 or x + count >= len(s))]
                elif strike == 1:
                    break
            array = set(array)

        return templast